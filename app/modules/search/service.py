"""Unified search across news, blogs, and coins.

A deliberately simple implementation: database ILIKE for news/blogs and an
in-memory filter over the cached coin list. This is the right amount of
machinery for V1 — a dedicated search engine can replace it later behind the
same service method if scale ever demands it.
"""

import logging

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ExternalServiceError
from app.modules.blog.models import Blog
from app.modules.blog.schemas import BlogSummary
from app.modules.market.schemas import Coin
from app.modules.market.service import MarketService
from app.modules.news.models import NewsArticle
from app.modules.news.schemas import NewsArticleOut
from app.modules.search.schemas import SearchResults

logger = logging.getLogger(__name__)

_LIMIT_PER_TYPE = 5


class SearchService:
    def __init__(self, db: AsyncSession, market_service: MarketService) -> None:
        self._db = db
        self._market = market_service

    async def search(self, query: str) -> SearchResults:
        return SearchResults(
            query=query,
            news=await self._search_news(query),
            blogs=await self._search_blogs(query),
            coins=await self._search_coins(query),
        )

    async def _search_news(self, query: str) -> list[NewsArticleOut]:
        pattern = f"%{query}%"
        stmt = (
            select(NewsArticle)
            .where(
                or_(
                    NewsArticle.title.ilike(pattern),
                    NewsArticle.description.ilike(pattern),
                )
            )
            .order_by(NewsArticle.published_at.desc())
            .limit(_LIMIT_PER_TYPE)
        )
        rows = (await self._db.execute(stmt)).scalars().all()
        return [NewsArticleOut.model_validate(row) for row in rows]

    async def _search_blogs(self, query: str) -> list[BlogSummary]:
        pattern = f"%{query}%"
        stmt = (
            select(Blog)
            .where(or_(Blog.title.ilike(pattern), Blog.excerpt.ilike(pattern)))
            .order_by(Blog.published_at.desc())
            .limit(_LIMIT_PER_TYPE)
        )
        rows = (await self._db.execute(stmt)).scalars().all()
        return [BlogSummary.model_validate(row) for row in rows]

    async def _search_coins(self, query: str) -> list[Coin]:
        try:
            coins = await self._market.get_top_coins(limit=100)
        except ExternalServiceError:
            logger.warning("search: coin list unavailable")
            return []

        needle = query.lower()
        matches = [
            coin
            for coin in coins
            if needle in coin.name.lower() or needle in coin.symbol.lower()
        ]
        return matches[:_LIMIT_PER_TYPE]
