"""blogs: add source, external_id, external_url for external providers

Revision ID: 0002_blog_source
Revises: 0001_initial
Create Date: 2026-08-13
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0002_blog_source"
down_revision: str | None = "0001_initial"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "blogs",
        sa.Column("source", sa.String(length=32), nullable=False, server_default="internal"),
    )
    op.add_column("blogs", sa.Column("external_id", sa.String(length=255), nullable=True))
    op.add_column("blogs", sa.Column("external_url", sa.String(length=1024), nullable=True))

    op.create_index("ix_blogs_source", "blogs", ["source"])
    op.create_unique_constraint("uq_blogs_external_id", "blogs", ["external_id"])


def downgrade() -> None:
    op.drop_constraint("uq_blogs_external_id", "blogs", type_="unique")
    op.drop_index("ix_blogs_source", table_name="blogs")
    op.drop_column("blogs", "external_url")
    op.drop_column("blogs", "external_id")
    op.drop_column("blogs", "source")
