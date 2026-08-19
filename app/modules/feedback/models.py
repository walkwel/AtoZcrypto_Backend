from datetime import datetime
from enum import StrEnum

from sqlalchemy import DateTime, ForeignKey, Index, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Sentiment(StrEnum):
    """How the respondent feels overall — the survey's one required answer."""

    LOVE = "love"
    OKAY = "okay"
    UNHAPPY = "unhappy"


class FeedbackStatus(StrEnum):
    """Triage state, owned by the admin reviewing the queue."""

    NEW = "new"
    REVIEWED = "reviewed"
    ARCHIVED = "archived"


class Feedback(Base):
    """One completed feedback survey.

    Every field except `sentiment` is optional: the survey lets people answer
    what they care about and skip the rest, and a partial response is still
    signal. Rows are immutable apart from `status`, which is the reviewer's
    triage flag — feedback is a historical record, not editable content.

    `user_id` is nullable and set only when the submitter was signed in;
    feedback is deliberately accepted anonymously, and deleting an account
    nulls the link rather than destroying the response.
    """

    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(primary_key=True)

    sentiment: Mapped[str] = mapped_column(String(16), index=True)
    # Only collected when the sentiment is negative — "what's not working?".
    sentiment_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    rating: Mapped[int | None] = mapped_column(Integer, nullable=True, index=True)
    feature_request: Mapped[str | None] = mapped_column(Text, nullable=True)
    review: Mapped[str | None] = mapped_column(Text, nullable=True)

    status: Mapped[str] = mapped_column(String(16), default=FeedbackStatus.NEW, index=True)

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    __table_args__ = (
        # The admin queue's default view is "newest first, filtered by status",
        # and the analytics roll-ups group by sentiment over a date window —
        # both are served by these composite indexes without a table scan.
        Index("ix_feedback_status_created_at", "status", "created_at"),
        Index("ix_feedback_sentiment_created_at", "sentiment", "created_at"),
    )
