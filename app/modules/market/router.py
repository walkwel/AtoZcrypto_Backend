"""Market HTTP endpoints."""

from typing import Annotated

from fastapi import APIRouter, Query

from app.modules.market.dependencies import MarketServiceDep
from app.modules.market.schemas import Coin, MarketChartPoint, MarketSummary

router = APIRouter(prefix="/markets", tags=["markets"])


@router.get("", response_model=list[Coin])
async def list_markets(
    service: MarketServiceDep,
    limit: Annotated[int, Query(ge=1, le=100)] = 50,
) -> list[Coin]:
    return await service.get_top_coins(limit=limit)


@router.get("/summary", response_model=MarketSummary)
async def market_summary(service: MarketServiceDep) -> MarketSummary:
    return await service.get_summary()


@router.get("/trending", response_model=list[Coin])
async def trending_markets(
    service: MarketServiceDep,
    limit: Annotated[int, Query(ge=1, le=10)] = 5,
) -> list[Coin]:
    return await service.get_trending(limit=limit)


@router.get("/chart", response_model=list[MarketChartPoint])
async def market_chart(
    service: MarketServiceDep,
    range: Annotated[str, Query(pattern="^(1D|1W|1M|3M|1Y|ALL)$")] = "1W",
    coin_id: Annotated[str, Query(min_length=1, max_length=64)] = "bitcoin",
) -> list[MarketChartPoint]:
    return await service.get_chart(range_key=range, coin_id=coin_id)
