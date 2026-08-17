"""CoinGecko public API implementation of MarketProvider.

Uses the free, keyless endpoints. Responses are parsed defensively so a
missing field on one coin never breaks the whole list.
"""

from app.core.config import Settings
from app.integrations.http_client import request_json
from app.modules.market.providers.base import MarketProvider
from app.modules.market.schemas import Coin, MarketChartPoint, MarketSummary


class CoinGeckoProvider(MarketProvider):
    def __init__(self, settings: Settings) -> None:
        self._base_url = settings.coingecko_base_url

    async def get_top_coins(self, *, limit: int = 50) -> list[Coin]:
        payload = await request_json(
            f"{self._base_url}/coins/markets",
            params={
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": limit,
                "page": 1,
                "sparkline": "true",
                "price_change_percentage": "24h",
            },
            provider="coingecko",
        )
        return [self._parse_coin(item) for item in payload if item.get("id")]

    async def get_global_summary(self) -> MarketSummary:
        payload = await request_json(f"{self._base_url}/global", provider="coingecko")
        data = payload.get("data", {})
        return MarketSummary(
            total_market_cap=float(data.get("total_market_cap", {}).get("usd", 0.0)),
            total_volume_24h=float(data.get("total_volume", {}).get("usd", 0.0)),
            btc_dominance=float(data.get("market_cap_percentage", {}).get("btc", 0.0)),
            market_cap_change_24h=self._safe_float(
                data.get("market_cap_change_percentage_24h_usd")
            ),
        )

    async def get_market_chart(self, *, coin_id: str, days: str) -> list[MarketChartPoint]:
        payload = await request_json(
            f"{self._base_url}/coins/{coin_id}/market_chart",
            params={"vs_currency": "usd", "days": days},
            provider="coingecko",
        )
        prices = payload.get("prices", [])
        return [
            MarketChartPoint(timestamp=int(point[0]), price=float(point[1]))
            for point in prices
            if len(point) == 2
        ]

    def _parse_coin(self, item: dict) -> Coin:
        sparkline = (item.get("sparkline_in_7d") or {}).get("price") or []
        return Coin(
            id=str(item["id"]),
            symbol=str(item.get("symbol", "")).upper(),
            name=str(item.get("name", "")),
            image=item.get("image"),
            price=self._safe_float(item.get("current_price")) or 0.0,
            change_24h=self._safe_float(item.get("price_change_percentage_24h")),
            market_cap=self._safe_float(item.get("market_cap")),
            volume_24h=self._safe_float(item.get("total_volume")),
            # Downsample the 7d sparkline to keep payloads small.
            sparkline=[round(float(p), 4) for p in sparkline[::6]] if sparkline else [],
        )

    @staticmethod
    def _safe_float(value: object) -> float | None:
        if value is None:
            return None
        try:
            return float(value)  # type: ignore[arg-type]
        except (TypeError, ValueError):
            return None
