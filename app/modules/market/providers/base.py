"""Market data provider interface.

The service depends on this contract, not on CoinGecko specifics, so an
alternative source can be added later without touching business logic.
"""

from abc import ABC, abstractmethod

from app.modules.market.schemas import Coin, MarketChartPoint, MarketSummary


class MarketProvider(ABC):
    @abstractmethod
    async def get_top_coins(self, *, limit: int = 50) -> list[Coin]:
        raise NotImplementedError

    @abstractmethod
    async def get_global_summary(self) -> MarketSummary:
        raise NotImplementedError

    @abstractmethod
    async def get_market_chart(self, *, coin_id: str, days: str) -> list[MarketChartPoint]:
        raise NotImplementedError
