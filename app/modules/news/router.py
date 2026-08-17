"""News HTTP endpoints. Only request/response concerns live here."""

from typing import Annotated

from fastapi import APIRouter, Query

from app.core.schemas import Page
from app.modules.news.dependencies import NewsServiceDep
from app.modules.news.schemas import NewsArticleOut, NewsCategory

router = APIRouter(prefix="/news", tags=["news"])


@router.get("", response_model=Page[NewsArticleOut])
async def list_news(
    service: NewsServiceDep,
    category: Annotated[str | None, Query()] = None,
    search: Annotated[str | None, Query(min_length=1, max_length=100)] = None,
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=50)] = 20,
) -> Page[NewsArticleOut]:
    return await service.list_news(category=category, search=search, page=page, limit=limit)


@router.get("/trending", response_model=list[NewsArticleOut])
async def trending_news(
    service: NewsServiceDep,
    limit: Annotated[int, Query(ge=1, le=10)] = 5,
) -> list[NewsArticleOut]:
    return await service.list_trending(limit)


@router.get("/categories", response_model=list[NewsCategory])
async def news_categories(service: NewsServiceDep) -> list[NewsCategory]:
    return service.categories()
