"""Feedback HTTP endpoints.

Submitting is open: the survey is offered to everyone, and requiring an account
to complain is how you stop hearing from the people most worth hearing from. If
the caller happens to be signed in, the response is linked to their account.

Everything else — reading, triaging, deleting — requires the admin role.
"""

from typing import Annotated

from fastapi import APIRouter, Query, status

from app.core.schemas import Page
from app.modules.auth.dependencies import OptionalUser, RequireAdmin
from app.modules.feedback.dependencies import FeedbackServiceDep
from app.modules.feedback.models import FeedbackStatus, Sentiment
from app.modules.feedback.schemas import (
    FeedbackCreate,
    FeedbackItem,
    FeedbackStatusUpdate,
    FeedbackSubmitted,
    FeedbackSummary,
)

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.post("", response_model=FeedbackSubmitted, status_code=status.HTTP_201_CREATED)
async def submit_feedback(
    payload: FeedbackCreate,
    service: FeedbackServiceDep,
    claims: OptionalUser,
) -> FeedbackSubmitted:
    feedback = await service.submit(payload, user_id=claims.user_id if claims else None)
    return FeedbackSubmitted(id=feedback.id, created_at=feedback.created_at)


# Declared before /{feedback_id} so the literal path wins the match.
@router.get("/summary", response_model=FeedbackSummary, dependencies=[RequireAdmin])
async def feedback_summary(
    service: FeedbackServiceDep,
    days: Annotated[int, Query(ge=1, le=365)] = 30,
) -> FeedbackSummary:
    return await service.summary(days=days)


@router.get("", response_model=Page[FeedbackItem], dependencies=[RequireAdmin])
async def list_feedback(
    service: FeedbackServiceDep,
    sentiment: Annotated[Sentiment | None, Query()] = None,
    feedback_status: Annotated[FeedbackStatus | None, Query(alias="status")] = None,
    rating: Annotated[int | None, Query(ge=1, le=5)] = None,
    search: Annotated[str | None, Query(max_length=200)] = None,
    days: Annotated[int | None, Query(ge=1, le=365)] = None,
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> Page[FeedbackItem]:
    return await service.list_feedback(
        sentiment=sentiment,
        status=feedback_status,
        rating=rating,
        search=search,
        days=days,
        page=page,
        limit=limit,
    )


@router.patch("/{feedback_id}", response_model=FeedbackItem, dependencies=[RequireAdmin])
async def update_feedback_status(
    feedback_id: int,
    payload: FeedbackStatusUpdate,
    service: FeedbackServiceDep,
) -> FeedbackItem:
    return FeedbackItem.model_validate(await service.set_status(feedback_id, payload.status))


@router.delete(
    "/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[RequireAdmin]
)
async def delete_feedback(feedback_id: int, service: FeedbackServiceDep) -> None:
    await service.delete(feedback_id)
