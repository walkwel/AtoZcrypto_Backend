"""RSS/XML → RawBlog normalisation.

Pure functions, no I/O — the reader does the fetching, this module does the
parsing, which is what makes it testable against fixtures instead of the live
web. One parser serves every feed: publisher differences are handled by trying
the standard RSS elements in a documented order, never by branching on source.

Shapes this handles, verified against the live Cointelegraph and CoinDesk feeds:
  * `<guid isPermaLink="true">` holding the canonical URL (Cointelegraph) and
    `isPermaLink="false"` holding an opaque UUID (CoinDesk).
  * `<link>` carrying UTM tracking parameters (Cointelegraph).
  * `<description>` as HTML with an inline `<img>` (Cointelegraph) or as plain
    text (CoinDesk).
  * Images in `<media:content>`, `<enclosure>`, or the description markup.
  * One `<category>` per item (Cointelegraph) or many (CoinDesk).
  * Repeated `<dc:creator>` elements for co-authored posts (CoinDesk).
"""

import hashlib
import logging
from dataclasses import dataclass, field
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from xml.etree import ElementTree

from app.modules.blog.providers.base import RawBlog
from app.modules.blog.providers.rss.feeds import RssFeed

logger = logging.getLogger(__name__)

_DC = "{http://purl.org/dc/elements/1.1/}"
_MEDIA = "{http://search.yahoo.com/mrss/}"

# Query parameters that identify the referrer rather than the article. Stripping
# them is what lets the same story fetched from two feeds dedupe to one row.
_TRACKING_PREFIXES = ("utm_",)
_TRACKING_PARAMS = frozenset({"ref", "referrer", "source", "fbclid", "gclid", "at_medium"})

_MAX_EXCERPT_CHARS = 500

# Feed taxonomies are publisher-specific and open-ended ("Latest News", "MiCA",
# "Bitcoin News", …). We map them onto the small taxonomy the product filters
# on; the untouched feed values are kept in `tags`. First rule that matches a
# tag wins, so order encodes precedence.
_CATEGORY_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("regulation", ("regulation", "policy", "legal", "lawsuit", "sec", "mica", "clarity act")),
    ("ethereum", ("ethereum", "ether")),
    ("defi", ("defi", "decentralized finance", "stablecoin", "tokenization", "real world asset")),
    ("markets", ("market", "price", "trading", "derivative", "bitcoin", "etf", "funding")),
)
DEFAULT_CATEGORY = "insights"


@dataclass(slots=True)
class FeedParseResult:
    """Parsed articles plus the counters the reader logs for observability."""

    articles: list[RawBlog] = field(default_factory=list)
    total_items: int = 0
    skipped: int = 0


def parse_feed(xml_text: str, feed: RssFeed) -> FeedParseResult:
    """Parse one RSS document into normalised articles.

    A malformed document yields an empty result rather than raising — one bad
    feed must not take down the others. Individual items that lack the fields we
    cannot do without (a title and a usable link) are skipped and counted.
    """
    try:
        root = ElementTree.fromstring(xml_text)
    except ElementTree.ParseError as exc:
        logger.warning(
            "rss parse failed", extra={"source": feed.slug, "error": str(exc)}
        )
        return FeedParseResult()

    items = root.findall(".//item") or root.findall(".//{http://www.w3.org/2005/Atom}entry")
    result = FeedParseResult(total_items=len(items))
    for item in items:
        article = _parse_item(item, feed)
        if article is None:
            result.skipped += 1
        else:
            result.articles.append(article)
    return result


def _parse_item(item: ElementTree.Element, feed: RssFeed) -> RawBlog | None:
    title = _text(item.findtext("title"))
    url = _article_url(item)
    if not title or url is None:
        return None

    description_html = item.findtext("description") or ""
    text, embedded_image = _strip_html(description_html)
    tags = _tags(item)

    return RawBlog(
        external_id=_dedup_key(url, item, feed),
        title=title,
        external_url=url,
        source=feed.slug,
        source_name=feed.name,
        published_at=_published_at(item),
        excerpt=_truncate(text) or None,
        author=_author(item, feed),
        category=_category(tags),
        cover_image_url=_image(item) or embedded_image,
        tags=tags,
    )


# --- field extraction ---------------------------------------------------------


def _article_url(item: ElementTree.Element) -> str | None:
    """The canonical article URL.

    A permalink `<guid>` is preferred: publishers that append tracking
    parameters to `<link>` (Cointelegraph does) still expose the clean URL here.
    """
    guid = item.find("guid")
    if guid is not None and (guid.get("isPermaLink") or "").lower() == "true":
        canonical = _canonical_url(guid.text)
        if canonical:
            return canonical
    return _canonical_url(item.findtext("link"))


def _dedup_key(url: str, item: ElementTree.Element, feed: RssFeed) -> str:
    """Stable identity for an article, hashed to a fixed-width column value.

    The canonical URL is the identifier of choice: it is stable across refreshes
    *and* identical when a story is syndicated into more than one feed, which is
    the duplicate users would actually notice. A feed `<guid>` is the fallback
    for items whose link we could not canonicalise; it is namespaced by source
    because guids are only unique within a publisher.

    Hashed because URLs exceed the column width, and a truncated URL could
    collide with a genuinely different article.
    """
    guid = _text(item.findtext("guid"))
    identity = url or f"{feed.slug}:{guid}"
    return hashlib.sha256(identity.encode("utf-8")).hexdigest()


def _published_at(item: ElementTree.Element) -> datetime:
    """Publication time, defaulting to now when absent or unparseable.

    A missing date is the one field we cannot leave empty — it orders the feed —
    so an item without one sorts as "just arrived", which is what a fresh RSS
    item almost always is.
    """
    raw = _text(item.findtext("pubDate")) or _text(item.findtext(_DC + "date"))
    if not raw:
        return datetime.now(UTC)
    try:
        # RSS 2.0 mandates RFC 2822 ("Mon, 17 Aug 2026 03:42:48 +0000").
        parsed = parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        try:
            parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            return datetime.now(UTC)
    # Feeds occasionally omit the offset; treat those as UTC rather than storing
    # a naive datetime into a timezone-aware column.
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)


def _author(item: ElementTree.Element, feed: RssFeed) -> str | None:
    """Byline from `<dc:creator>`/`<author>`, or None when the feed omits it."""
    names = [_text(el.text) for el in item.findall(_DC + "creator")]
    names = [name for name in names if name]
    if not names:
        single = _text(item.findtext("author"))
        names = [single] if single else []
    if not names:
        return None

    # Some feeds prefix the byline with the publication ("Cointelegraph by Ada
    # Lovelace"). Drop it — the publisher is already shown as the source.
    prefix = f"{feed.name.lower()} by "
    cleaned = [
        name[len(prefix) :].strip() if name.lower().startswith(prefix) else name
        for name in names
    ]
    return ", ".join(dict.fromkeys(filter(None, cleaned))) or None


def _image(item: ElementTree.Element) -> str | None:
    """Cover image from `<media:content>` or an image `<enclosure>`."""
    media = item.find(_MEDIA + "content")
    if media is not None and media.get("url"):
        return media.get("url")

    thumbnail = item.find(_MEDIA + "thumbnail")
    if thumbnail is not None and thumbnail.get("url"):
        return thumbnail.get("url")

    enclosure = item.find("enclosure")
    if enclosure is not None and (enclosure.get("type") or "").startswith("image/"):
        return enclosure.get("url")
    return None


def _tags(item: ElementTree.Element) -> list[str]:
    """Feed categories, verbatim, de-duplicated and order-preserving."""
    values = (_text(el.text) for el in item.findall("category"))
    return list(dict.fromkeys(value for value in values if value))


def _category(tags: list[str]) -> str:
    """Map feed tags onto our taxonomy, defaulting to the general bucket."""
    lowered = [tag.lower() for tag in tags]
    for category, keywords in _CATEGORY_RULES:
        if any(keyword in tag for tag in lowered for keyword in keywords):
            return category
    return DEFAULT_CATEGORY


# --- text helpers -------------------------------------------------------------


class _HtmlTextExtractor(HTMLParser):
    """Strips markup from a description, capturing the first inline image."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []
        self.first_image: str | None = None

    def handle_data(self, data: str) -> None:
        self._chunks.append(data)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "img" and self.first_image is None:
            self.first_image = dict(attrs).get("src") or None

    @property
    def text(self) -> str:
        return " ".join("".join(self._chunks).split())


def _strip_html(raw: str) -> tuple[str, str | None]:
    """Return (plain text, first embedded image URL) for a description body."""
    if not raw:
        return "", None
    parser = _HtmlTextExtractor()
    try:
        parser.feed(raw)
        parser.close()
    except Exception:  # noqa: BLE001 — malformed markup degrades to what we parsed
        logger.debug("rss description markup could not be fully parsed")
    return parser.text, parser.first_image


def _truncate(text: str) -> str:
    """Trim an excerpt to a card-sized length, breaking on a word boundary.

    RSS summaries are metadata we are licensed to show; the full article stays
    with the publisher, which is why nothing here reads the article body.
    """
    if len(text) <= _MAX_EXCERPT_CHARS:
        return text
    clipped = text[:_MAX_EXCERPT_CHARS].rsplit(" ", 1)[0].rstrip(",.;:—-")
    return f"{clipped}…"


def _canonical_url(raw: str | None) -> str | None:
    """Normalise an article URL, dropping tracking parameters and fragments.

    Returns None for anything that is not an absolute http(s) URL, so callers
    can treat "no usable link" as a skip.
    """
    value = _text(raw)
    if not value:
        return None
    try:
        parts = urlsplit(value)
    except ValueError:
        return None
    if parts.scheme.lower() not in ("http", "https") or not parts.netloc:
        return None

    query = urlencode(
        [
            (key, value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
            if not key.lower().startswith(_TRACKING_PREFIXES)
            and key.lower() not in _TRACKING_PARAMS
        ]
    )
    return urlunsplit(
        (parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), query, "")
    )


def _text(value: str | None) -> str:
    return (value or "").strip()
