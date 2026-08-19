"""Academy curriculum: phased modules, timed lessons, per-user progress

The Academy grew from a short FAQ into a structured programme, which changes
three things:

  * `course_modules` gains `phase` — the stage of the journey a module belongs
    to, so fifteen modules read as five phases rather than one long list.
  * `course_lessons` becomes a lesson rather than a question: `question`/`answer`
    are renamed to `title`/`body`, and each lesson carries its own
    `duration_minutes` (module totals are summed from these) and a `kind` that
    separates reading from homework.
  * `course_lesson_completions` records that one user finished one lesson. A row
    *is* the completion — un-completing deletes it — and the unique constraint
    keeps marking idempotent so a double submit cannot inflate progress.

Renaming preserves the existing content; no module has to be re-authored.

Revision ID: 0006_academy_curriculum
Revises: 0005_feedback_courses
Create Date: 2026-08-18
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0006_academy_curriculum"
down_revision: str | None = "0005_feedback_courses"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "course_modules",
        sa.Column("phase", sa.String(length=32), nullable=False, server_default="foundations"),
    )
    op.create_index("ix_course_modules_phase", "course_modules", ["phase"])

    op.alter_column(
        "course_lessons",
        "question",
        new_column_name="title",
        existing_type=sa.String(length=512),
        existing_nullable=False,
    )
    op.alter_column(
        "course_lessons",
        "answer",
        new_column_name="body",
        existing_type=sa.Text(),
        existing_nullable=False,
    )
    op.add_column(
        "course_lessons",
        sa.Column("kind", sa.String(length=16), nullable=False, server_default="lesson"),
    )
    op.add_column(
        "course_lessons",
        sa.Column("duration_minutes", sa.Integer(), nullable=False, server_default="8"),
    )

    op.create_table(
        "course_lesson_completions",
        sa.Column("id", sa.Integer(), primary_key=True),
        # Both sides cascade: a deleted account and a deleted lesson each leave
        # a completion with nothing to describe.
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "lesson_id",
            sa.Integer(),
            sa.ForeignKey("course_lessons.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "completed_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.UniqueConstraint("user_id", "lesson_id", name="uq_lesson_completion_user_lesson"),
    )
    op.create_index("ix_course_lesson_completions_user_id", "course_lesson_completions", ["user_id"])
    op.create_index(
        "ix_course_lesson_completions_lesson_id", "course_lesson_completions", ["lesson_id"]
    )


def downgrade() -> None:
    op.drop_table("course_lesson_completions")

    op.drop_column("course_lessons", "duration_minutes")
    op.drop_column("course_lessons", "kind")
    op.alter_column(
        "course_lessons",
        "body",
        new_column_name="answer",
        existing_type=sa.Text(),
        existing_nullable=False,
    )
    op.alter_column(
        "course_lessons",
        "title",
        new_column_name="question",
        existing_type=sa.String(length=512),
        existing_nullable=False,
    )

    op.drop_index("ix_course_modules_phase", table_name="course_modules")
    op.drop_column("course_modules", "phase")
