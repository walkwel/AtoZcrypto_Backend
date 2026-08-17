"""Dashboard HTTP endpoint — a single aggregated call for the overview page."""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.modules.blog.dependencies import get_blog_service
from app.modules.blog.service import BlogService
from app.modules.dashboard.schemas import DashboardResponse
from app.modules.dashboard.service import DashboardService
from app.modules.market.dependencies import get_market_service
from app.modules.market.service import MarketService
from app.modules.news.dependencies import get_news_service
from app.modules.news.service import NewsService

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


def get_dashboard_service(
    news_service: Annotated[NewsService, Depends(get_news_service)],
    market_service: Annotated[MarketService, Depends(get_market_service)],
    blog_service: Annotated[BlogService, Depends(get_blog_service)],
) -> DashboardService:
    return DashboardService(news_service, market_service, blog_service)


@router.get("", response_model=DashboardResponse)
async def get_dashboard(
    service: Annotated[DashboardService, Depends(get_dashboard_service)],
) -> DashboardResponse:
    return await service.get_overview()
