"""feedback surveys and Academy course content

Adds two independent features:

  * `feedback` — one row per submitted survey. Indexed for the two access
    patterns the admin dashboard has: the triage queue (status + newest first)
    and the analytics roll-ups (sentiment/rating over a date window).
  * `course_modules` / `course_lessons` — educational content moved out of the
    frontend bundle so editors can change it without a deploy. Lessons cascade
    with their module; a module without its lessons is not a meaningful record.

Revision ID: 0005_feedback_courses
Revises: 0004_blog_rss
Create Date: 2026-08-18
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0005_feedback_courses"
down_revision: str | None = "0004_blog_rss"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "feedback",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("sentiment", sa.String(length=16), nullable=False),
        sa.Column("sentiment_note", sa.Text(), nullable=True),
        sa.Column("rating", sa.Integer(), nullable=True),
        sa.Column("feature_request", sa.Text(), nullable=True),
        sa.Column("review", sa.Text(), nullable=True),
        sa.Column("status", sa.String(length=16), nullable=False, server_default="new"),
        # Anonymous submissions are expected, and deleting an account must not
        # delete the feedback it left behind.
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index("ix_feedback_sentiment", "feedback", ["sentiment"])
    op.create_index("ix_feedback_rating", "feedback", ["rating"])
    op.create_index("ix_feedback_status", "feedback", ["status"])
    op.create_index("ix_feedback_user_id", "feedback", ["user_id"])
    op.create_index("ix_feedback_created_at", "feedback", ["created_at"])
    op.create_index("ix_feedback_status_created_at", "feedback", ["status", "created_at"])
    op.create_index("ix_feedback_sentiment_created_at", "feedback", ["sentiment", "created_at"])

    op.create_table(
        "course_modules",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("level", sa.String(length=32), nullable=False, server_default="beginner"),
        sa.Column("position", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("is_published", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index("ix_course_modules_slug", "course_modules", ["slug"], unique=True)
    op.create_index("ix_course_modules_level", "course_modules", ["level"])
    op.create_index("ix_course_modules_position", "course_modules", ["position"])
    op.create_index("ix_course_modules_is_published", "course_modules", ["is_published"])

    op.create_table(
        "course_lessons",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "module_id",
            sa.Integer(),
            sa.ForeignKey("course_modules.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("question", sa.String(length=512), nullable=False),
        sa.Column("answer", sa.Text(), nullable=False),
        sa.Column("position", sa.Integer(), nullable=False, server_default="0"),
    )
    op.create_index("ix_course_lessons_module_id", "course_lessons", ["module_id"])


def downgrade() -> None:
    op.drop_table("course_lessons")
    op.drop_table("course_modules")
    op.drop_table("feedback")
