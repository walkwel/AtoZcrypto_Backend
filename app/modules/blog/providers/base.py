"""External blog provider interface.

A provider fetches articles from upstream sources and normalises them into
`RawBlog` — our internal, provider-agnostic shape. The service depends only on
this interface, so the concrete source (today: RSS feeds) can change without
touching business logic.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class RawBlog:
    """One normalised external article.

    Optional fields are `None`/empty when the upstream feed genuinely does not
    provide them — we never substitute invented values. `external_id` is the
    deduplication key (see providers/rss/parser.py), not a publisher id.
    """

    external_id: str
    title: str
    external_url: str
    source: str
    source_name: str
    published_at: datetime
    excerpt: str | None = None
    author: str | None = None
    category: str = "insights"
    cover_image_url: str | None = None
    tags: list[str] = field(default_factory=list)


class BlogProvider(ABC):
    @abstractmethod
    async def fetch_latest(self, *, limit: int = 30) -> list[RawBlog]:
        """Fetch the most recent external blog articles, newest first."""
        raise NotImplementedError
