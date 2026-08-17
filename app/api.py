"""Aggregates every module router under the /api/v1 prefix."""

from fastapi import APIRouter

from app.modules.auth.router import router as auth_router
from app.modules.blog.router import router as blog_router
from app.modules.dashboard.router import router as dashboard_router
from app.modules.health.router import router as health_router
from app.modules.market.router import router as market_router
from app.modules.news.router import router as news_router
from app.modules.search.router import router as search_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(dashboard_router)
api_router.include_router(news_router)
api_router.include_router(market_router)
api_router.include_router(blog_router)
api_router.include_router(search_router)
