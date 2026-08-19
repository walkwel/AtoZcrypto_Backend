"""Feedback API contracts.

Two audiences, two shapes: the public submission payload (`FeedbackCreate`) and
the reviewer's view (`FeedbackItem`, `FeedbackSummary`). Nothing internal —
user ids, raw row state — is exposed on the public side.
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.modules.feedback.models import FeedbackStatus, Sentiment

# Generous but bounded: enough for a considered answer, small enough that a
# single row can never be used to push megabytes into the database.
_MAX_TEXT = 2000


def _clean(value: str | None) -> str | None:
    """Whitespace-only answers are the same as no answer at all."""
    if value is None:
        return None
    trimmed = value.strip()
    return trimmed or None


class FeedbackCreate(BaseModel):
    """A submitted survey. Only the sentiment is required."""

    sentiment: Sentiment
    sentiment_note: str | None = Field(default=None, max_length=_MAX_TEXT)
    rating: int | None = Field(default=None, ge=1, le=5)
    feature_request: str | None = Field(default=None, max_length=_MAX_TEXT)
    review: str | None = Field(default=None, max_length=_MAX_TEXT)

    @field_validator("sentiment_note", "feature_request", "review", mode="after")
    @classmethod
    def _normalise_text(cls, value: str | None) -> str | None:
        return _clean(value)


class FeedbackSubmitted(BaseModel):
    """Acknowledgement returned to the submitter — no reviewer-only fields."""

    id: int
    created_at: datetime


class FeedbackItem(BaseModel):
    """A response as the admin queue shows it."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    sentiment: Sentiment
    sentiment_note: str | None
    rating: int | None
    feature_request: str | None
    review: str | None
    status: FeedbackStatus
    # Email of the submitter when they were signed in; None for anonymous
    # responses, which the survey accepts by design.
    submitted_by: str | None = None
    created_at: datetime


class FeedbackStatusUpdate(BaseModel):
    status: FeedbackStatus


class SentimentCount(BaseModel):
    sentiment: Sentiment
    count: int


class RatingCount(BaseModel):
    rating: int
    count: int


class DailyCount(BaseModel):
    day: date
    count: int


class FeedbackSummary(BaseModel):
    """Everything the analytics view needs, in one round trip.

    Computed by aggregate queries in the database rather than by loading rows,
    so the cost is independent of how much feedback has been collected.
    """

    total: int
    total_in_window: int
    window_days: int
    new_count: int
    average_rating: float | None
    rated_count: int
    promoter_share: float
    by_sentiment: list[SentimentCount]
    by_rating: list[RatingCount]
    daily: list[DailyCount]
