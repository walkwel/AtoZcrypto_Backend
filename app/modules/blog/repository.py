"""Database access for blogs. No business logic, no HTTP concerns."""

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.blog.models import Blog
from app.modules.blog.providers.base import RawBlog
from app.modules.blog.slug import slugify


class BlogRepository:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def list_blogs(
        self,
        *,
        category: str | None = None,
        source: str | None = None,
        page: int = 1,
        limit: int = 12,
    ) -> tuple[list[Blog], int]:
        base = select(Blog)
        if category:
            base = base.where(Blog.category == category)
        if source:
            base = base.where(Blog.source == source)

        total = await self._db.scalar(select(func.count()).select_from(base.subquery())) or 0

        query = (
            base.order_by(Blog.published_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        rows = list((await self._db.execute(query)).scalars().all())
        return rows, total

    async def get_by_slug(self, slug: str) -> Blog | None:
        return await self._db.scalar(select(Blog).where(Blog.slug == slug))

    async def slug_exists(self, slug: str) -> bool:
        return await self._db.scalar(select(Blog.id).where(Blog.slug == slug)) is not None

    async def list_latest(self, limit: int = 3) -> list[Blog]:
        query = select(Blog).order_by(Blog.published_at.desc()).limit(limit)
        return list((await self._db.execute(query)).scalars().all())

    async def list_related(self, *, category: str, exclude_slug: str, limit: int = 3) -> list[Blog]:
        query = (
            select(Blog)
            .where(Blog.category == category, Blog.slug != exclude_slug)
            .order_by(Blog.published_at.desc())
            .limit(limit)
        )
        return list((await self._db.execute(query)).scalars().all())

    # --- writes ---------------------------------------------------------------

    async def add(self, blog: Blog) -> Blog:
        self._db.add(blog)
        await self._db.commit()
        await self._db.refresh(blog)
        return blog

    async def save(self) -> None:
        await self._db.commit()

    async def delete(self, blog: Blog) -> None:
        await self._db.delete(blog)
        await self._db.commit()

    async def list_categories(self) -> list[str]:
        """Distinct categories that actually have articles, alphabetically."""
        query = select(Blog.category).distinct().order_by(Blog.category)
        return list((await self._db.execute(query)).scalars().all())

    async def upsert_external(self, blogs: list[RawBlog]) -> int:
        """Insert new external articles and refresh metadata on existing ones.

        Keyed on `external_id`, so repeated scheduled refreshes are idempotent.
        Uses a read-then-write rather than dialect-specific ON CONFLICT: the
        batch is one refresh's worth of articles, and portable SQL means this
        path is covered by the test suite instead of stubbed out.

        Returns the number of rows inserted (updates are not counted as writes).
        """
        if not blogs:
            return 0

        external_ids = [blog.external_id for blog in blogs]
        existing_rows = (
            await self._db.execute(select(Blog).where(Blog.external_id.in_(external_ids)))
        ).scalars()
        existing = {row.external_id: row for row in existing_rows}

        inserted = 0
        for blog in blogs:
            current = existing.get(blog.external_id)
            if current is None:
                self._db.add(await self._build_external(blog))
                inserted += 1
            else:
                self._apply_external(current, blog)

        await self._db.commit()
        return inserted

    async def _build_external(self, blog: RawBlog) -> Blog:
        row = Blog(
            slug=await self._unique_external_slug(blog),
            content="",  # the article body stays with the publisher
            source=blog.source,
            external_id=blog.external_id,
            published_at=blog.published_at,
        )
        self._apply_external(row, blog)
        return row

    @staticmethod
    def _apply_external(row: Blog, blog: RawBlog) -> None:
        """Copy the mutable metadata a feed can revise after first publication."""
        row.title = blog.title
        row.excerpt = blog.excerpt or ""
        row.cover_image_url = blog.cover_image_url
        row.category = blog.category
        row.author = blog.author
        row.source_name = blog.source_name
        row.external_url = blog.external_url
        row.tags = blog.tags

    async def _unique_external_slug(self, blog: RawBlog) -> str:
        """Readable slug, disambiguated by a short prefix of the dedup hash."""
        base = f"{slugify(blog.title)[:200]}-{blog.external_id[:8]}"
        if not await self.slug_exists(base):
            return base
        # Different articles sharing a title *and* hash prefix is vanishingly
        # rare; widen the suffix rather than fail the whole refresh.
        return f"{slugify(blog.title)[:180]}-{blog.external_id[:24]}"[:255]
