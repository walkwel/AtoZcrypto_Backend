"""RSS feed registry — the single place blog sources are configured.

Adding a publisher is a one-line change here: append an `RssFeed`. The reader
and parser are source-agnostic, so no other file needs to change. Feeds can be
narrowed at runtime with the BLOG_RSS_FEEDS setting (see `enabled_feeds`).
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RssFeed:
    """A single RSS source.

    slug:     stable machine key, persisted as `Blog.source`
    name:     publisher display name, shown to users for attribution
    feed_url: the RSS document to fetch
    site_url: the publisher's homepage, for attribution links
    """

    slug: str
    name: str
    feed_url: str
    site_url: str


FEEDS: tuple[RssFeed, ...] = (
    RssFeed(
        slug="cointelegraph",
        name="Cointelegraph",
        feed_url="https://cointelegraph.com/rss",
        site_url="https://cointelegraph.com",
    ),
    RssFeed(
        slug="coindesk",
        name="CoinDesk",
        feed_url="https://www.coindesk.com/arc/outboundfeeds/rss/",
        site_url="https://www.coindesk.com",
    ),
)

FEEDS_BY_SLUG: dict[str, RssFeed] = {feed.slug: feed for feed in FEEDS}


def enabled_feeds(selection: str = "") -> tuple[RssFeed, ...]:
    """Resolve which feeds are active.

    `selection` is the comma-separated BLOG_RSS_FEEDS setting: a list of slugs
    from FEEDS. Empty (the default) enables every registered feed. Unknown slugs
    are ignored so a typo degrades to "fewer feeds", never a boot failure.
    """
    slugs = [slug.strip().lower() for slug in selection.split(",") if slug.strip()]
    if not slugs:
        return FEEDS
    return tuple(FEEDS_BY_SLUG[slug] for slug in slugs if slug in FEEDS_BY_SLUG)
