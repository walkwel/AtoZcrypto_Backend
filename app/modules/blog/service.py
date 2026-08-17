"""Blog business logic.

Handles both platform-owned (internal) blogs — full CRUD for the writer — and
external articles aggregated from publisher RSS feeds. External articles are
read-only: they are refreshed from the provider and cannot be edited or deleted
through the admin API.

Depends on the BlogProvider *interface* and the repository — never on a concrete
feed reader or the DB driver directly.
"""

import logging
import time
from datetime import UTC, datetime

from app.core.config import Settings
from app.core.exceptions import ExternalServiceError, ForbiddenError, NotFoundError, ValidationError
from app.core.redis import Cache
from app.core.schemas import Page
from app.modules.blog.models import BLOG_SOURCE_INTERNAL, Blog
from app.modules.blog.providers.base import BlogProvider
from app.modules.blog.repository import BlogRepository
from app.modules.blog.schemas import (
    BlogCategory,
    BlogCreate,
    BlogDetail,
    BlogSummary,
    BlogUpdate,
)
from app.modules.blog.slug import estimate_reading_time, slugify

logger = logging.getLogger(__name__)

_CACHE_PREFIX = "blogs"
_GENERATION_KEY = f"{_CACHE_PREFIX}:generation"

# Category slugs whose display form isn't simple title-casing.
_CATEGORY_LABELS = {"defi": "DeFi", "nft": "NFT"}


class BlogWithRelated(BlogDetail):
    related: list[BlogSummary] = []


class BlogService:
    def __init__(
        self,
        repository: BlogRepository,
        cache: Cache,
        settings: Settings,
        provider: BlogProvider | None = None,
    ) -> None:
        self._repo = repository
        self._cache = cache
        self._ttl = settings.blog_cache_ttl
        self._provider = provider

    # --- reads ----------------------------------------------------------------

    async def list_blogs(
        self,
        *,
        category: str | None = None,
        source: str | None = None,
        page: int = 1,
        limit: int = 12,
    ) -> Page[BlogSummary]:
        cache_key = await self._feed_cache_key(category, source, page, limit)
        cached = await self._cache.get_json(cache_key)
        if cached is not None:
            return Page[BlogSummary].model_validate(cached)

        rows, total = await self._repo.list_blogs(
            category=category, source=source, page=page, limit=limit
        )
        result = Page.create(
            [BlogSummary.model_validate(row) for row in rows], page, limit, total
        )
        await self._cache.set_json(cache_key, result.model_dump(mode="json"), self._ttl)
        return result

    async def get_blog(self, slug: str) -> BlogWithRelated:
        blog = await self._require_blog(slug)
        related = await self._repo.list_related(
            category=blog.category, exclude_slug=blog.slug, limit=3
        )
        detail = BlogWithRelated.model_validate(blog)
        detail.related = [BlogSummary.model_validate(row) for row in related]
        return detail

    async def list_latest(self, limit: int = 3) -> list[BlogSummary]:
        rows = await self._repo.list_latest(limit)
        return [BlogSummary.model_validate(row) for row in rows]

    async def list_categories(self) -> list[BlogCategory]:
        """Filter options, derived from the articles actually stored.

        Deriving these keeps the filters honest as feeds come and go, instead of
        a hardcoded list drifting out of sync with the content.
        """
        slugs = await self._repo.list_categories()
        return [BlogCategory(slug="all", label="All")] + [
            BlogCategory(slug=slug, label=self._category_label(slug)) for slug in slugs
        ]

    @staticmethod
    def _category_label(slug: str) -> str:
        return _CATEGORY_LABELS.get(slug, slug.replace("-", " ").title())

    # --- writes (internal blogs only) ----------------------------------------

    async def create_blog(self, data: BlogCreate) -> BlogDetail:
        slug = await self._unique_slug(data.slug or slugify(data.title))
        blog = Blog(
            slug=slug,
            title=data.title,
            excerpt=data.excerpt,
            content=data.content,
            cover_image_url=data.cover_image_url,
            category=data.category,
            author=data.author,
            reading_time_minutes=data.reading_time_minutes
            or estimate_reading_time(data.content),
            source=BLOG_SOURCE_INTERNAL,
            published_at=datetime.now(UTC),
        )
        saved = await self._repo.add(blog)
        await self._invalidate_cache()
        return BlogDetail.model_validate(saved)

    async def update_blog(self, slug: str, data: BlogUpdate) -> BlogDetail:
        blog = await self._require_editable(slug)

        fields = data.model_dump(exclude_unset=True)
        for key, value in fields.items():
            setattr(blog, key, value)
        # Keep reading time in sync when the body changes.
        if "content" in fields:
            blog.reading_time_minutes = estimate_reading_time(blog.content)

        await self._repo.save()
        await self._invalidate_cache()
        return BlogDetail.model_validate(blog)

    async def delete_blog(self, slug: str) -> None:
        blog = await self._require_editable(slug)
        await self._repo.delete(blog)
        await self._invalidate_cache()

    # --- external refresh -----------------------------------------------------

    async def refresh_external(self, *, limit: int = 60) -> int:
        """Pull the latest articles from the RSS provider and persist them.

        Individual feed failures are already contained by the provider; a total
        provider failure is logged and treated as "nothing new this run" so the
        scheduled job never crashes and existing articles keep serving.
        """
        if self._provider is None:
            return 0

        try:
            blogs = await self._provider.fetch_latest(limit=limit)
        except ExternalServiceError as exc:
            logger.warning("blog refresh failed", extra={"error": str(exc)})
            return 0

        written = await self._repo.upsert_external(blogs)
        if written:
            await self._invalidate_cache()
        logger.info("blog refresh complete", extra={"fetched": len(blogs), "written": written})
        return written

    # --- helpers --------------------------------------------------------------

    async def _require_blog(self, slug: str) -> Blog:
        blog = await self._repo.get_by_slug(slug)
        if blog is None:
            raise NotFoundError(f"Blog '{slug}' not found.")
        return blog

    async def _require_editable(self, slug: str) -> Blog:
        blog = await self._require_blog(slug)
        if blog.source != BLOG_SOURCE_INTERNAL:
            raise ForbiddenError("External blogs are read-only and cannot be modified.")
        return blog

    async def _unique_slug(self, base: str) -> str:
        base = base[:240] or "post"
        if not await self._repo.slug_exists(base):
            return base
        # Append an incrementing suffix until the slug is free.
        for suffix in range(2, 1000):
            candidate = f"{base}-{suffix}"
            if not await self._repo.slug_exists(candidate):
                return candidate
        raise ValidationError("Could not generate a unique slug for this title.")

    async def _invalidate_cache(self) -> None:
        """Drop cached listings after a write.

        Listings are cached per filter combination, which is too many keys to
        track individually and the Cache interface has no wildcard delete. So the
        keys carry a generation stamp: dropping it makes the next read mint a new
        one, orphaning every previously cached listing to expire on its own TTL.
        """
        await self._cache.delete(_GENERATION_KEY)

    async def _generation(self) -> str:
        """Current cache generation, created on demand.

        A missing generation only costs a round of cache misses, so losing it
        (eviction, Redis restart) is safe by construction.
        """
        cached = await self._cache.get_json(_GENERATION_KEY)
        if cached is not None:
            return str(cached)
        generation = str(time.time_ns())
        await self._cache.set_json(_GENERATION_KEY, generation, self._ttl)
        return generation

    async def _feed_cache_key(
        self, category: str | None, source: str | None, page: int, limit: int
    ) -> str:
        generation = await self._generation()
        return (
            f"{_CACHE_PREFIX}:list:{generation}:"
            f"{category or 'all'}:{source or 'all'}:{page}:{limit}"
        )
