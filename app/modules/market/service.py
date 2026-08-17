"""Market business logic: fetch live data via the provider, cache in Redis.

Market data is inherently live, so it is not persisted to Postgres — Redis is
the right store for short-lived snapshots. If Redis is unavailable, every call
degrades to a direct provider fetch.
"""

import logging

from app.core.config import Settings
from app.core.redis import Cache
from app.modules.market.providers.base import MarketProvider
from app.modules.market.schemas import Coin, MarketChartPoint, MarketSummary

logger = logging.getLogger(__name__)

_TOP_COINS_KEY = "market:top_coins"
_SUMMARY_KEY = "market:summary"
_TRENDING_KEY = "market:trending"

# Map dashboard range buttons to CoinGecko's `days` parameter.
_RANGE_TO_DAYS: dict[str, str] = {
    "1D": "1",
    "1W": "7",
    "1M": "30",
    "3M": "90",
    "1Y": "365",
    "ALL": "max",
}


class MarketService:
    def __init__(self, provider: MarketProvider, cache: Cache, settings: Settings) -> None:
        self._provider = provider
        self._cache = cache
        self._ttl = settings.market_cache_ttl

    async def get_top_coins(self, *, limit: int = 50) -> list[Coin]:
        cached = await self._cache.get_json(_TOP_COINS_KEY)
        if cached is not None:
            return [Coin.model_validate(c) for c in cached][:limit]

        coins = await self._provider.get_top_coins(limit=100)
        await self._cache.set_json(
            _TOP_COINS_KEY, [c.model_dump() for c in coins], self._ttl
        )
        return coins[:limit]

    async def get_summary(self) -> MarketSummary:
        cached = await self._cache.get_json(_SUMMARY_KEY)
        if cached is not None:
            return MarketSummary.model_validate(cached)

        summary = await self._provider.get_global_summary()
        await self._cache.set_json(_SUMMARY_KEY, summary.model_dump(), self._ttl)
        return summary

    async def get_trending(self, *, limit: int = 5) -> list[Coin]:
        """Top movers by absolute 24h change, drawn from the cached top coins."""
        coins = await self.get_top_coins(limit=100)
        ranked = sorted(coins, key=lambda c: abs(c.change_24h or 0.0), reverse=True)
        return ranked[:limit]

    async def get_chart(
        self, *, range_key: str = "1W", coin_id: str = "bitcoin"
    ) -> list[MarketChartPoint]:
        days = _RANGE_TO_DAYS.get(range_key.upper(), "7")
        cache_key = f"market:chart:{coin_id}:{days}"
        cached = await self._cache.get_json(cache_key)
        if cached is not None:
            return [MarketChartPoint.model_validate(p) for p in cached]

        points = await self._provider.get_market_chart(coin_id=coin_id, days=days)
        await self._cache.set_json(cache_key, [p.model_dump() for p in points], self._ttl)
        return points
