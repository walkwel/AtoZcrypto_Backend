from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class BlogSummary(BaseModel):
    """Card-level fields for listing pages (no full content).

    Deliberately provider-independent: no feed identifiers, publisher-specific
    fields, or raw RSS structure reaches the client. `source` is our own slug
    and `source_name` is the publisher's display name used for attribution.
    Optional fields are null when the upstream feed does not supply them.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    excerpt: str
    cover_image_url: str | None
    category: str
    author: str | None
    reading_time_minutes: int | None
    source: str
    source_name: str | None
    external_url: str | None
    tags: list[str] = []
    published_at: datetime

    @field_validator("tags", mode="before")
    @classmethod
    def _default_tags(cls, value: list[str] | None) -> list[str]:
        """The column is null for internal posts; the API always returns a list."""
        return value or []


class BlogDetail(BlogSummary):
    """Full article including body content.

    For external articles `content` is empty by design — we store and show only
    metadata plus an excerpt, and link readers to the original publisher.
    """

    content: str


class BlogCategory(BaseModel):
    """A category filter option, derived from the articles actually stored."""

    slug: str
    label: str


class BlogCreate(BaseModel):
    """Payload to author a new internal blog."""

    title: str = Field(min_length=3, max_length=512)
    excerpt: str = Field(min_length=3, max_length=1000)
    content: str = Field(min_length=1)
    category: str = Field(default="insights", max_length=64)
    author: str = Field(min_length=1, max_length=255)
    cover_image_url: str | None = Field(default=None, max_length=1024)
    # Optional overrides; computed from title/content when omitted.
    slug: str | None = Field(default=None, max_length=255)
    reading_time_minutes: int | None = Field(default=None, ge=1, le=120)


class BlogUpdate(BaseModel):
    """Partial update for an internal blog. Only provided fields change."""

    title: str | None = Field(default=None, min_length=3, max_length=512)
    excerpt: str | None = Field(default=None, min_length=3, max_length=1000)
    content: str | None = Field(default=None, min_length=1)
    category: str | None = Field(default=None, max_length=64)
    author: str | None = Field(default=None, min_length=1, max_length=255)
    cover_image_url: str | None = Field(default=None, max_length=1024)
