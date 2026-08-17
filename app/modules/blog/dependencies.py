"""FastAPI dependency wiring for the blog module."""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.core.database import get_db
from app.core.redis import Cache, get_cache
from app.modules.blog.providers.rss.reader import RssBlogProvider
from app.modules.blog.repository import BlogRepository
from app.modules.blog.service import BlogService


def get_blog_service(
    db: Annotated[AsyncSession, Depends(get_db)],
    cache: Annotated[Cache, Depends(get_cache)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> BlogService:
    return BlogService(BlogRepository(db), cache, settings, RssBlogProvider(settings))


BlogServiceDep = Annotated[BlogService, Depends(get_blog_service)]
