"""FastAPI dependency wiring for the courses module."""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.core.database import get_db
from app.core.redis import Cache, get_cache
from app.modules.courses.repository import CourseRepository, ProgressRepository
from app.modules.courses.service import CourseService, ProgressService


def get_course_service(
    db: Annotated[AsyncSession, Depends(get_db)],
    cache: Annotated[Cache, Depends(get_cache)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> CourseService:
    return CourseService(CourseRepository(db), cache, settings)


def get_progress_service(db: Annotated[AsyncSession, Depends(get_db)]) -> ProgressService:
    """Progress reads the curriculum but never caches it — see ProgressService."""
    return ProgressService(CourseRepository(db), ProgressRepository(db))


CourseServiceDep = Annotated[CourseService, Depends(get_course_service)]
ProgressServiceDep = Annotated[ProgressService, Depends(get_progress_service)]
