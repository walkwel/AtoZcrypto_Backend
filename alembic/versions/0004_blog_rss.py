"""blogs: RSS article metadata (source_name, tags, updated_at) and drop Dev.to rows

Replaces the Dev.to blog integration with RSS aggregation:
  * adds `source_name` (publisher display name) and `tags` (feed categories),
  * adds `updated_at` so refreshed article metadata is auditable,
  * relaxes `author` and `reading_time_minutes` to nullable — RSS feeds do not
    always supply a byline and never supply a reading time, and we do not
    substitute invented values,
  * deletes the previously mirrored Dev.to rows, whose `external_id` values used
    the old provider's id scheme and can never match an RSS dedup key.

Revision ID: 0004_blog_rss
Revises: 0003_auth
Create Date: 2026-08-17
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0004_blog_rss"
down_revision: str | None = "0003_auth"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("blogs", sa.Column("source_name", sa.String(length=128), nullable=True))
    op.add_column("blogs", sa.Column("tags", sa.JSON(), nullable=True))
    op.add_column(
        "blogs",
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    op.alter_column("blogs", "author", existing_type=sa.String(length=255), nullable=True)
    op.alter_column("blogs", "reading_time_minutes", existing_type=sa.Integer(), nullable=True)

    # Mirrored Dev.to articles are no longer reachable by any provider. Internal
    # (platform-authored) blogs are untouched.
    op.execute(sa.text("DELETE FROM blogs WHERE source = 'devto'"))


def downgrade() -> None:
    # Rows with no author/reading time would violate the restored NOT NULL
    # constraints, so backfill them before tightening the columns.
    op.execute(sa.text("UPDATE blogs SET author = source_name WHERE author IS NULL"))
    op.execute(sa.text("UPDATE blogs SET author = 'Unknown' WHERE author IS NULL"))
    op.execute(
        sa.text("UPDATE blogs SET reading_time_minutes = 5 WHERE reading_time_minutes IS NULL")
    )

    op.alter_column("blogs", "reading_time_minutes", existing_type=sa.Integer(), nullable=False)
    op.alter_column("blogs", "author", existing_type=sa.String(length=255), nullable=False)

    op.drop_column("blogs", "updated_at")
    op.drop_column("blogs", "tags")
    op.drop_column("blogs", "source_name")
