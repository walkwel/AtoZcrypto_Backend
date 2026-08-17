"""FastAPI dependency wiring for the news module.

Keeps construction of repository → provider → service in one place so the
router stays thin and the pieces stay swappable in tests.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.core.database import get_db
from app.core.redis import Cache, get_cache
from app.modules.news.providers.newsdata import NewsDataProvider
from app.modules.news.repository import NewsRepository
from app.modules.news.service import NewsService


def get_news_service(
    db: Annotated[AsyncSession, Depends(get_db)],
    cache: Annotated[Cache, Depends(get_cache)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> NewsService:
    provider = NewsDataProvider(settings)
    repository = NewsRepository(db)
    return NewsService(repository, provider, cache, settings)


NewsServiceDep = Annotated[NewsService, Depends(get_news_service)]
