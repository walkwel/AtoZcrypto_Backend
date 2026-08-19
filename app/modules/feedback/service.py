"""Feedback business logic.

Submission is intentionally cheap — one insert — because it sits on a user
interaction. Analytics are the expensive side, so they are aggregated in SQL
and cached briefly; a dashboard that is a minute stale is fine, a dashboard
that scans the table on every refresh is not.
"""

import logging
from datetime import UTC, datetime, timedelta

from app.core.config import Settings
from app.core.exceptions import NotFoundError
from app.core.redis import Cache
from app.core.schemas import Page
from app.modules.feedback.models import Feedback, FeedbackStatus, Sentiment
from app.modules.feedback.repository import FeedbackRepository
from app.modules.feedback.schemas import (
    DailyCount,
    FeedbackCreate,
    FeedbackItem,
    FeedbackSummary,
    RatingCount,
    SentimentCount,
)

logger = logging.getLogger(__name__)

_SUMMARY_KEY = "feedback:summary"
_SUMMARY_TTL = 60
# The windows the dashboard offers, and therefore the only ones worth caching:
# they are the keys a write must invalidate, so caching exactly this set keeps
# invalidation exact. An ad-hoc window (days=45) is computed live rather than
# cached under a key nothing would ever clear.
_CACHED_WINDOWS = frozenset({7, 30, 90})
# Ratings of 4 and 5 count as promoters, mirroring how NPS-style scores are
# usually banded. Named here so the dashboard and any future report agree.
_PROMOTER_MIN_RATING = 4


class FeedbackService:
    def __init__(self, repository: FeedbackRepository, cache: Cache, settings: Settings) -> None:
        self._repository = repository
        self._cache = cache
        self._settings = settings

    async def submit(self, payload: FeedbackCreate, *, user_id: int | None = None) -> Feedback:
        feedback = await self._repository.add(
            Feedback(
                sentiment=payload.sentiment,
                # The follow-up prompt only appears for unhappy respondents, so
                # a note attached to a positive answer is dropped rather than
                # stored under a question that was never asked.
                sentiment_note=(
                    payload.sentiment_note if payload.sentiment == Sentiment.UNHAPPY else None
                ),
                rating=payload.rating,
                feature_request=payload.feature_request,
                review=payload.review,
                user_id=user_id,
            )
        )
        # The dashboard should reflect a new response immediately.
        await self._invalidate()
        logger.info("feedback submitted", extra={"sentiment": payload.sentiment})
        return feedback

    async def list_feedback(
        self,
        *,
        sentiment: str | None = None,
        status: str | None = None,
        rating: int | None = None,
        search: str | None = None,
        days: int | None = None,
        page: int = 1,
        limit: int = 20,
    ) -> Page[FeedbackItem]:
        rows, total = await self._repository.list_feedback(
            sentiment=sentiment,
            status=status,
            rating=rating,
            search=search,
            since=_window_start(days) if days else None,
            page=page,
            limit=limit,
        )
        items = [
            FeedbackItem.model_validate(feedback).model_copy(update={"submitted_by": email})
            for feedback, email in rows
        ]
        return Page.create(items, page=page, limit=limit, total=total)

    async def set_status(self, feedback_id: int, status: FeedbackStatus) -> Feedback:
        feedback = await self._require(feedback_id)
        feedback.status = status
        await self._repository.save()
        await self._invalidate()
        return feedback

    async def delete(self, feedback_id: int) -> None:
        await self._repository.delete(await self._require(feedback_id))
        await self._invalidate()

    async def summary(self, *, days: int = 30) -> FeedbackSummary:
        if days not in _CACHED_WINDOWS:
            return await self._build_summary(days)

        cache_key = _summary_key(days)
        cached = await self._cache.get_json(cache_key)
        if cached is not None:
            return FeedbackSummary.model_validate(cached)

        summary = await self._build_summary(days)
        await self._cache.set_json(cache_key, summary.model_dump(mode="json"), _SUMMARY_TTL)
        return summary

    async def _build_summary(self, days: int) -> FeedbackSummary:
        since = _window_start(days)

        total = await self._repository.count_all()
        total_in_window = await self._repository.count_since(since)
        new_count = await self._repository.count_by_status(FeedbackStatus.NEW)
        sentiments = await self._repository.count_by_sentiment(since)
        ratings = await self._repository.count_by_rating(since)
        average_rating, rated_count = await self._repository.rating_stats(since)
        daily = await self._repository.count_by_day(since)

        promoters = sum(
            count for rating, count in ratings.items() if rating >= _PROMOTER_MIN_RATING
        )

        return FeedbackSummary(
            total=total,
            total_in_window=total_in_window,
            window_days=days,
            new_count=new_count,
            average_rating=round(average_rating, 2) if average_rating is not None else None,
            rated_count=rated_count,
            promoter_share=round(promoters / rated_count * 100, 1) if rated_count else 0.0,
            # Every bucket is always present, including the empty ones: a chart
            # with a missing bar reads as "no data" rather than "none of these".
            by_sentiment=[
                SentimentCount(sentiment=value, count=sentiments.get(value, 0))
                for value in Sentiment
            ],
            by_rating=[
                RatingCount(rating=value, count=ratings.get(value, 0)) for value in range(1, 6)
            ],
            daily=_fill_days(daily, since=since, days=days),
        )

    async def _invalidate(self) -> None:
        """Drop every cached window, so no view of the data can go stale."""
        await self._cache.delete(*(_summary_key(days) for days in _CACHED_WINDOWS))

    async def _require(self, feedback_id: int) -> Feedback:
        feedback = await self._repository.get(feedback_id)
        if feedback is None:
            raise NotFoundError("Feedback not found.")
        return feedback


def _summary_key(days: int) -> str:
    return f"{_SUMMARY_KEY}:{days}"


def _window_start(days: int) -> datetime:
    """Midnight UTC `days - 1` days ago, so "7 days" means seven whole days."""
    start_of_today = datetime.now(UTC).replace(hour=0, minute=0, second=0, microsecond=0)
    return start_of_today - timedelta(days=max(days - 1, 0))


def _fill_days(counts: dict, *, since: datetime, days: int) -> list[DailyCount]:
    """A dense series — one point per day, zeros included.

    Trend charts must not draw a straight line across a quiet day; the gap is
    the information.
    """
    first = since.date()
    series = []
    for offset in range(days):
        day = first + timedelta(days=offset)
        series.append(DailyCount(day=day, count=counts.get(day, 0)))
    return series
