"""FastAPI dependency wiring for the market module."""

from typing import Annotated

from fastapi import Depends

from app.core.config import Settings, get_settings
from app.core.redis import Cache, get_cache
from app.modules.market.providers.coingecko import CoinGeckoProvider
from app.modules.market.service import MarketService


def get_market_service(
    cache: Annotated[Cache, Depends(get_cache)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> MarketService:
    provider = CoinGeckoProvider(settings)
    return MarketService(provider, cache, settings)


MarketServiceDep = Annotated[MarketService, Depends(get_market_service)]
