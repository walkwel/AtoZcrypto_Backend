"""RSS blog provider: fetch the configured feeds, normalise, deduplicate.

Feeds are fetched concurrently and each one is isolated — a publisher that is
down, slow, or serving malformed XML costs us that source's articles and nothing
else. The parsing itself lives in parser.py; this module owns I/O, failure
handling, and merging the sources into one ordered list.
"""

import asyncio
import logging
import time

from app.core.config import Settings
from app.integrations.http_client import request_text
from app.modules.blog.providers.base import BlogProvider, RawBlog
from app.modules.blog.providers.rss.feeds import RssFeed, enabled_feeds
from app.modules.blog.providers.rss.parser import parse_feed

logger = logging.getLogger(__name__)

# Some publishers reject requests without a User-Agent.
_HEADERS = {
    "User-Agent": "AtoZCrypto/1.0 (+https://github.com/atoz-crypto)",
    "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
}


class RssBlogProvider(BlogProvider):
    def __init__(self, settings: Settings) -> None:
        self._feeds = enabled_feeds(settings.blog_rss_feeds)

    async def fetch_latest(self, *, limit: int = 30) -> list[RawBlog]:
        if not self._feeds:
            logger.warning("no RSS feeds enabled — blog refresh has nothing to fetch")
            return []

        results = await asyncio.gather(
            *(self._fetch_feed(feed) for feed in self._feeds),
            return_exceptions=True,
        )

        articles: list[RawBlog] = []
        for feed, result in zip(self._feeds, results, strict=True):
            if isinstance(result, BaseException):
                # Already logged with detail in _fetch_feed; the other sources
                # continue so the Blogs page stays populated.
                logger.warning(
                    "rss source unavailable",
                    extra={"source": feed.slug, "error": str(result)},
                )
                continue
            articles.extend(result)

        return self._merge(articles, limit)

    async def _fetch_feed(self, feed: RssFeed) -> list[RawBlog]:
        started = time.perf_counter()
        xml_text = await request_text(feed.feed_url, provider=feed.slug, headers=_HEADERS)
        result = parse_feed(xml_text, feed)
        logger.info(
            "rss feed fetched",
            extra={
                "source": feed.slug,
                "items": result.total_items,
                "accepted": len(result.articles),
                "skipped": result.skipped,
                "latency_ms": round((time.perf_counter() - started) * 1000, 1),
            },
        )
        return result.articles

    @staticmethod
    def _merge(articles: list[RawBlog], limit: int) -> list[RawBlog]:
        """Order newest-first and drop duplicates, keeping the freshest copy.

        Sorting before de-duplicating means a syndicated article is represented
        by whichever feed published it first in our ordering, deterministically.
        """
        articles.sort(key=lambda article: article.published_at, reverse=True)

        unique: dict[str, RawBlog] = {}
        for article in articles:
            unique.setdefault(article.external_id, article)

        duplicates = len(articles) - len(unique)
        if duplicates:
            logger.info("rss duplicates removed", extra={"duplicates": duplicates})
        return list(unique.values())[:limit]
