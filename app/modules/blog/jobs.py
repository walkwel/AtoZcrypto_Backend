"""Scheduled external-blog refresh.

Builds its own short-lived DB session (it runs outside the request lifecycle)
and delegates to BlogService.refresh_external. Registered by the scheduler in
main.py — the same in-process mechanism the news refresh already uses.
"""

from app.core.config import get_settings
from app.core.database import SessionFactory
from app.core.redis import get_cache
from app.modules.blog.providers.rss.reader import RssBlogProvider
from app.modules.blog.repository import BlogRepository
from app.modules.blog.service import BlogService


async def refresh_blogs_job() -> None:
    settings = get_settings()
    async with SessionFactory() as db:
        service = BlogService(
            BlogRepository(db), get_cache(), settings, RssBlogProvider(settings)
        )
        await service.refresh_external()
