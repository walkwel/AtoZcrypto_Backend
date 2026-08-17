"""Dashboard aggregation.

Composes the news, market, and blog services into one payload. Market data
comes from an external API, so a market failure must not blank out news and
blogs — that section degrades to empty instead of failing the whole request.
"""

import asyncio
import logging

from app.core.exceptions import ExternalServiceError
from app.modules.blog.service import BlogService
from app.modules.dashboard.schemas import DashboardResponse
from app.modules.market.schemas import Coin, MarketSummary
from app.modules.market.service import MarketService
from app.modules.news.service import NewsService

logger = logging.getLogger(__name__)


class DashboardService:
    def __init__(
        self,
        news_service: NewsService,
        market_service: MarketService,
        blog_service: BlogService,
    ) -> None:
        self._news = news_service
        self._market = market_service
        self._blog = blog_service

    async def get_overview(self) -> DashboardResponse:
        # Market calls are HTTP-only (no DB) and safe to run concurrently.
        summary, top_coins, trending = await asyncio.gather(
            self._safe_summary(),
            self._safe_top_coins(),
            self._safe_trending(),
        )
        # News and blogs share the request's AsyncSession, which is NOT safe for
        # concurrent use — run them sequentially on the same session.
        latest_news = await self._news.list_news(page=1, limit=5)
        latest_blogs = await self._blog.list_latest(limit=3)

        return DashboardResponse(
            market_summary=summary,
            top_coins=top_coins,
            trending=trending,
            latest_news=latest_news.data,
            latest_blogs=latest_blogs,
        )

    async def _safe_summary(self) -> MarketSummary | None:
        try:
            return await self._market.get_summary()
        except ExternalServiceError:
            logger.warning("dashboard: market summary unavailable")
            return None

    async def _safe_top_coins(self) -> list[Coin]:
        try:
            return await self._market.get_top_coins(limit=8)
        except ExternalServiceError:
            logger.warning("dashboard: top coins unavailable")
            return []

    async def _safe_trending(self) -> list[Coin]:
        try:
            return await self._market.get_trending(limit=5)
        except ExternalServiceError:
            logger.warning("dashboard: trending unavailable")
            return []
