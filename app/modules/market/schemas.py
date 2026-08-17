from pydantic import BaseModel


class Coin(BaseModel):
    id: str
    symbol: str
    name: str
    image: str | None
    price: float
    change_24h: float | None
    market_cap: float | None
    volume_24h: float | None
    sparkline: list[float] = []


class MarketSummary(BaseModel):
    total_market_cap: float
    total_volume_24h: float
    btc_dominance: float
    market_cap_change_24h: float | None


class MarketChartPoint(BaseModel):
    timestamp: int
    price: float
