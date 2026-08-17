from pydantic import BaseModel

from app.modules.blog.schemas import BlogSummary
from app.modules.market.schemas import Coin, MarketSummary
from app.modules.news.schemas import NewsArticleOut


class DashboardResponse(BaseModel):
    """Everything the dashboard needs in a single call.

    Reuses each module's public schema so the dashboard never invents a parallel
    shape that could drift from the dedicated pages.
    """

    market_summary: MarketSummary | None
    top_coins: list[Coin]
    trending: list[Coin]
    latest_news: list[NewsArticleOut]
    latest_blogs: list[BlogSummary]
