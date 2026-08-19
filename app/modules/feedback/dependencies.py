"""FastAPI dependency wiring for the feedback module."""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.core.database import get_db
from app.core.redis import Cache, get_cache
from app.modules.feedback.repository import FeedbackRepository
from app.modules.feedback.service import FeedbackService


def get_feedback_service(
    db: Annotated[AsyncSession, Depends(get_db)],
    cache: Annotated[Cache, Depends(get_cache)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> FeedbackService:
    return FeedbackService(FeedbackRepository(db), cache, settings)


FeedbackServiceDep = Annotated[FeedbackService, Depends(get_feedback_service)]
