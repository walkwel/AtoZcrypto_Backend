from datetime import datetime

from sqlalchemy import JSON, DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

# Blog origin. Internal blogs are authored on-platform and fully editable;
# external blogs are aggregated from publisher RSS feeds and are read-only.
# External source values are the feed slugs in providers/rss/feeds.py.
BLOG_SOURCE_INTERNAL = "internal"


class Blog(Base):
    """A blog article — either platform-owned (internal) or aggregated from an
    external RSS feed. Internal content is trusted but still rendered as plain
    text by the frontend; external articles store metadata and an excerpt only
    and link out to the publisher's canonical URL.
    """

    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    title: Mapped[str] = mapped_column(String(512))
    excerpt: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    cover_image_url: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    category: Mapped[str] = mapped_column(String(64), index=True, default="insights")
    author: Mapped[str | None] = mapped_column(String(255), nullable=True)
    # Nullable: RSS feeds do not report reading time and we do not invent one.
    reading_time_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    # Publisher-assigned topics, kept verbatim for filtering and debugging.
    tags: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)

    # Provenance. `external_*` fields are set only for feed-sourced articles.
    # `external_id` is the dedup key (a hash — see providers/rss/parser.py) and
    # is unique so repeated refreshes upsert cleanly.
    source: Mapped[str] = mapped_column(String(32), index=True, default=BLOG_SOURCE_INTERNAL)
    source_name: Mapped[str | None] = mapped_column(String(128), nullable=True)
    external_id: Mapped[str | None] = mapped_column(String(255), unique=True, nullable=True)
    external_url: Mapped[str | None] = mapped_column(String(1024), nullable=True)

    published_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
