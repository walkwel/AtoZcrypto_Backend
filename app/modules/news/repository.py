"""Database access for news articles. No business logic, no HTTP concerns."""

from sqlalchemy import func, or_, select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.news.models import NewsArticle
from app.modules.news.providers.base import RawArticle


class NewsRepository:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def upsert_many(self, articles: list[RawArticle]) -> int:
        """Insert new articles; skip ones already stored (by external_id).

        Returns the number of rows written. Uses PostgreSQL ON CONFLICT so a
        refresh is idempotent and cheap.
        """
        if not articles:
            return 0

        rows = [
            {
                "external_id": a.external_id,
                "title": a.title,
                "description": a.description,
                "source": a.source,
                "article_url": a.article_url,
                "image_url": a.image_url,
                "category": a.category,
                "published_at": a.published_at,
            }
            for a in articles
        ]
        stmt = (
            pg_insert(NewsArticle)
            .values(rows)
            .on_conflict_do_nothing(index_elements=["external_id"])
        )
        result = await self._db.execute(stmt)
        await self._db.commit()
        return result.rowcount or 0

    async def list_articles(
        self,
        *,
        category: str | None = None,
        search: str | None = None,
        page: int = 1,
        limit: int = 20,
    ) -> tuple[list[NewsArticle], int]:
        conditions = []
        if category:
            conditions.append(NewsArticle.category == category)
        if search:
            pattern = f"%{search}%"
            conditions.append(
                or_(NewsArticle.title.ilike(pattern), NewsArticle.description.ilike(pattern))
            )

        base = select(NewsArticle)
        for condition in conditions:
            base = base.where(condition)

        total = await self._db.scalar(select(func.count()).select_from(base.subquery())) or 0

        query = (
            base.order_by(NewsArticle.published_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        rows = list((await self._db.execute(query)).scalars().all())
        return rows, total

    async def list_trending(self, limit: int = 5) -> list[NewsArticle]:
        """Most recent articles stand in for 'trending' in V1."""
        query = select(NewsArticle).order_by(NewsArticle.published_at.desc()).limit(limit)
        return list((await self._db.execute(query)).scalars().all())
