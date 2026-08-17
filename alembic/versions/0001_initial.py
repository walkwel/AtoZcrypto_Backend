"""initial schema: news_articles, blogs

Revision ID: 0001_initial
Revises:
Create Date: 2026-08-01
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001_initial"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "news_articles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("external_id", sa.String(length=255), nullable=False),
        sa.Column("title", sa.String(length=512), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("source", sa.String(length=255), nullable=True),
        sa.Column("article_url", sa.String(length=1024), nullable=False),
        sa.Column("image_url", sa.String(length=1024), nullable=True),
        sa.Column("category", sa.String(length=64), nullable=False, server_default="markets"),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.UniqueConstraint("external_id", name="uq_news_articles_external_id"),
    )
    op.create_index("ix_news_articles_external_id", "news_articles", ["external_id"])
    op.create_index("ix_news_articles_category", "news_articles", ["category"])
    op.create_index("ix_news_articles_published_at", "news_articles", ["published_at"])
    op.create_index(
        "ix_news_category_published", "news_articles", ["category", "published_at"]
    )

    op.create_table(
        "blogs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("title", sa.String(length=512), nullable=False),
        sa.Column("excerpt", sa.Text(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("cover_image_url", sa.String(length=1024), nullable=True),
        sa.Column("category", sa.String(length=64), nullable=False, server_default="insights"),
        sa.Column("author", sa.String(length=255), nullable=False),
        sa.Column("reading_time_minutes", sa.Integer(), nullable=False, server_default="5"),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.UniqueConstraint("slug", name="uq_blogs_slug"),
    )
    op.create_index("ix_blogs_slug", "blogs", ["slug"])
    op.create_index("ix_blogs_category", "blogs", ["category"])
    op.create_index("ix_blogs_published_at", "blogs", ["published_at"])


def downgrade() -> None:
    op.drop_table("blogs")
    op.drop_table("news_articles")
