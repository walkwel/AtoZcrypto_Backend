"""News business logic: refresh from provider, read with caching and filtering.

Depends on the NewsProvider *interface* and the repository — never on a
concrete provider or the DB driver directly.
"""

import logging

from app.core.config import Settings
from app.core.redis import Cache
from app.core.schemas import Page
from app.modules.news.providers.base import NewsProvider
from app.modules.news.repository import NewsRepository
from app.modules.news.schemas import NEWS_CATEGORIES, NewsArticleOut, NewsCategory

logger = logging.getLogger(__name__)

_TRENDING_KEY = "news:trending"


class NewsService:
    def __init__(
        self,
        repository: NewsRepository,
        provider: NewsProvider,
        cache: Cache,
        settings: Settings,
    ) -> None:
        self._repo = repository
        self._provider = provider
        self._cache = cache
        self._ttl = settings.news_cache_ttl

    async def refresh(self, *, category: str | None = None) -> int:
        """Pull latest articles from the provider and persist new ones.

        Called by the background scheduler. Invalidates trending cache on write.
        """
        articles = await self._provider.fetch_latest(category=category, limit=50)
        written = await self._repo.upsert_many(articles)
        if written:
            await self._cache.delete(_TRENDING_KEY)
        logger.info("news refresh complete", extra={"fetched": len(articles), "written": written})
        return written

    async def list_news(
        self,
        *,
        category: str | None = None,
        search: str | None = None,
        page: int = 1,
        limit: int = 20,
    ) -> Page[NewsArticleOut]:
        normalized = self._normalize_category(category)

        # Only cache the common, unsearched category feeds. Searches and deep
        # pages are too varied to cache usefully.
        cache_key = self._feed_cache_key(normalized, page, limit) if not search else None
        if cache_key:
            cached = await self._cache.get_json(cache_key)
            if cached is not None:
                return Page[NewsArticleOut].model_validate(cached)

        rows, total = await self._repo.list_articles(
            category=normalized, search=search, page=page, limit=limit
        )
        result = Page.create(
            [NewsArticleOut.model_validate(row) for row in rows], page, limit, total
        )

        if cache_key:
            await self._cache.set_json(cache_key, result.model_dump(mode="json"), self._ttl)
        return result

    async def list_trending(self, limit: int = 5) -> list[NewsArticleOut]:
        cached = await self._cache.get_json(_TRENDING_KEY)
        if cached is not None:
            return [NewsArticleOut.model_validate(item) for item in cached]

        rows = await self._repo.list_trending(limit)
        result = [NewsArticleOut.model_validate(row) for row in rows]
        await self._cache.set_json(
            _TRENDING_KEY, [item.model_dump(mode="json") for item in result], self._ttl
        )
        return result

    @staticmethod
    def categories() -> list[NewsCategory]:
        return [NewsCategory(slug="all", label="All")] + [
            NewsCategory(slug=slug, label=slug.capitalize()) for slug in NEWS_CATEGORIES
        ]

    @staticmethod
    def _normalize_category(category: str | None) -> str | None:
        if not category or category == "all":
            return None
        return category if category in NEWS_CATEGORIES else None

    @staticmethod
    def _feed_cache_key(category: str | None, page: int, limit: int) -> str:
        scope = category or "latest"
        return f"news:category:{scope}:{page}:{limit}"
