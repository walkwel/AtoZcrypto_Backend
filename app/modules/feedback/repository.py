"""Database access for feedback. No business logic, no HTTP concerns.

The analytics queries here deliberately return aggregates, not rows: the admin
dashboard's cost stays flat as the table grows, because counting a million
responses happens in the database, not in Python.
"""

from datetime import date, datetime

from sqlalchemy import Row, Select, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.models import User
from app.modules.feedback.models import Feedback, FeedbackStatus


class FeedbackRepository:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    # --- writes ---------------------------------------------------------------

    async def add(self, feedback: Feedback) -> Feedback:
        self._db.add(feedback)
        await self._db.commit()
        await self._db.refresh(feedback)
        return feedback

    async def save(self) -> None:
        await self._db.commit()

    async def delete(self, feedback: Feedback) -> None:
        await self._db.delete(feedback)
        await self._db.commit()

    # --- reads ----------------------------------------------------------------

    async def get(self, feedback_id: int) -> Feedback | None:
        return await self._db.scalar(select(Feedback).where(Feedback.id == feedback_id))

    def _filtered(
        self,
        *,
        sentiment: str | None,
        status: str | None,
        rating: int | None,
        search: str | None,
        since: datetime | None,
    ) -> Select:
        """One filter builder shared by the list query and its count.

        Keeping them in sync matters: a count that applies different predicates
        than the page it describes produces a pager that lies.
        """
        query = select(Feedback)
        if sentiment:
            query = query.where(Feedback.sentiment == sentiment)
        if status:
            query = query.where(Feedback.status == status)
        if rating is not None:
            query = query.where(Feedback.rating == rating)
        if since is not None:
            query = query.where(Feedback.created_at >= since)
        if search:
            term = f"%{search.lower()}%"
            query = query.where(
                or_(
                    func.lower(Feedback.sentiment_note).like(term),
                    func.lower(Feedback.feature_request).like(term),
                    func.lower(Feedback.review).like(term),
                )
            )
        return query

    async def list_feedback(
        self,
        *,
        sentiment: str | None = None,
        status: str | None = None,
        rating: int | None = None,
        search: str | None = None,
        since: datetime | None = None,
        page: int = 1,
        limit: int = 20,
    ) -> tuple[list[Row], int]:
        """A page of responses with the submitter's email joined in.

        Rows are `(Feedback, email | None)` — a LEFT JOIN so anonymous
        responses are never dropped from the queue.
        """
        base = self._filtered(
            sentiment=sentiment, status=status, rating=rating, search=search, since=since
        )
        total = await self._db.scalar(select(func.count()).select_from(base.subquery())) or 0

        query = (
            base.add_columns(User.email)
            .outerjoin(User, User.id == Feedback.user_id)
            .order_by(Feedback.created_at.desc(), Feedback.id.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        return list((await self._db.execute(query)).all()), total

    # --- analytics ------------------------------------------------------------

    async def count_all(self) -> int:
        return await self._db.scalar(select(func.count(Feedback.id))) or 0

    async def count_since(self, since: datetime) -> int:
        return (
            await self._db.scalar(
                select(func.count(Feedback.id)).where(Feedback.created_at >= since)
            )
            or 0
        )

    async def count_by_status(self, status: FeedbackStatus) -> int:
        return (
            await self._db.scalar(
                select(func.count(Feedback.id)).where(Feedback.status == status)
            )
            or 0
        )

    async def count_by_sentiment(self, since: datetime) -> dict[str, int]:
        query = (
            select(Feedback.sentiment, func.count(Feedback.id))
            .where(Feedback.created_at >= since)
            .group_by(Feedback.sentiment)
        )
        return {row[0]: row[1] for row in (await self._db.execute(query)).all()}

    async def count_by_rating(self, since: datetime) -> dict[int, int]:
        query = (
            select(Feedback.rating, func.count(Feedback.id))
            .where(Feedback.created_at >= since, Feedback.rating.is_not(None))
            .group_by(Feedback.rating)
        )
        return {int(row[0]): row[1] for row in (await self._db.execute(query)).all()}

    async def rating_stats(self, since: datetime) -> tuple[float | None, int]:
        """Average rating and how many responses carried one."""
        query = select(func.avg(Feedback.rating), func.count(Feedback.rating)).where(
            Feedback.created_at >= since
        )
        average, rated = (await self._db.execute(query)).one()
        return (float(average) if average is not None else None), int(rated or 0)

    async def count_by_day(self, since: datetime) -> dict[date, int]:
        """Daily volume. `func.date` keeps this portable across Postgres and SQLite."""
        day = func.date(Feedback.created_at)
        query = (
            select(day, func.count(Feedback.id))
            .where(Feedback.created_at >= since)
            .group_by(day)
            .order_by(day)
        )
        rows = (await self._db.execute(query)).all()
        return {_as_date(row[0]): row[1] for row in rows}


def _as_date(value: date | datetime | str) -> date:
    """SQLite returns an ISO string from `date()`; Postgres returns a date."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value)[:10])
