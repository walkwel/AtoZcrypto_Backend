"""Scheduled news refresh job.

Builds its own short-lived DB session (it runs outside the request lifecycle)
and delegates all logic to NewsService.refresh. Registered by the scheduler in
main.py.
"""

import logging

from app.core.config import get_settings
from app.core.database import SessionFactory
from app.core.redis import get_cache
from app.modules.news.providers.newsdata import NewsDataProvider
from app.modules.news.repository import NewsRepository
from app.modules.news.service import NewsService

logger = logging.getLogger(__name__)


async def refresh_news_job() -> None:
    settings = get_settings()
    async with SessionFactory() as db:
        service = NewsService(
            repository=NewsRepository(db),
            provider=NewsDataProvider(settings),
            cache=get_cache(),
            settings=settings,
        )
        await service.refresh()
