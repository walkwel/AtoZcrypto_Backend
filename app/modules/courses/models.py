from datetime import datetime
from enum import StrEnum

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class CourseLevel(StrEnum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class CoursePhase(StrEnum):
    """The five stages a learner moves through, in order.

    A phase groups modules on the Academy page so a 15-module programme reads as
    a journey rather than a long list. It is deliberately a small fixed set: the
    curriculum's shape is an editorial decision, not a per-module free-text field.
    """

    FOUNDATIONS = "foundations"
    MARKET_MECHANICS = "market-mechanics"
    ANALYSIS = "analysis"
    RISK_AND_STRATEGY = "risk-and-strategy"
    PRACTICE = "practice"


class LessonKind(StrEnum):
    """What a lesson asks of the reader.

    `HOMEWORK` lessons are exercises rather than reading — the UI badges them and
    they close out a module.
    """

    LESSON = "lesson"
    HOMEWORK = "homework"


class CourseModule(Base):
    """A unit of educational content: a titled module holding ordered lessons.

    Modules are edited in the admin panel and read by the public Academy page.
    `position` drives the reading order (authors care about sequence), and
    `is_published` lets an editor draft a module without exposing it.
    """

    __tablename__ = "course_modules"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    summary: Mapped[str] = mapped_column(Text)
    level: Mapped[str] = mapped_column(String(32), default=CourseLevel.BEGINNER, index=True)
    phase: Mapped[str] = mapped_column(
        String(32), default=CoursePhase.FOUNDATIONS, index=True, server_default="foundations"
    )
    position: Mapped[int] = mapped_column(Integer, default=0, index=True)
    is_published: Mapped[bool] = mapped_column(Boolean, default=True, index=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # Lessons belong to their module: deleting a module deletes its lessons,
    # both in the database (ondelete) and in the session (cascade), so neither
    # path can leave orphans behind.
    lessons: Mapped[list["CourseLesson"]] = relationship(
        back_populates="module",
        cascade="all, delete-orphan",
        order_by="CourseLesson.position",
        lazy="selectin",
    )

    @property
    def duration_minutes(self) -> int:
        """Reading time for the whole module, summed from its lessons.

        Derived rather than stored so it can never disagree with the lessons it
        describes — an editor who deletes a lesson does not also have to
        remember to correct a total.
        """
        return sum(lesson.duration_minutes for lesson in self.lessons)


class CourseLesson(Base):
    """One lesson within a module — the Academy's teaching unit."""

    __tablename__ = "course_lessons"

    id: Mapped[int] = mapped_column(primary_key=True)
    module_id: Mapped[int] = mapped_column(
        ForeignKey("course_modules.id", ondelete="CASCADE"), index=True
    )
    title: Mapped[str] = mapped_column(String(512))
    body: Mapped[str] = mapped_column(Text)
    kind: Mapped[str] = mapped_column(
        String(16), default=LessonKind.LESSON, server_default="lesson"
    )
    duration_minutes: Mapped[int] = mapped_column(Integer, default=8, server_default="8")
    position: Mapped[int] = mapped_column(Integer, default=0)

    module: Mapped[CourseModule] = relationship(back_populates="lessons")


class LessonCompletion(Base):
    """A record that one user finished one lesson.

    Presence is the fact: a row means complete, no row means not started, so
    un-completing a lesson deletes the row rather than flipping a flag. The
    unique constraint makes "complete" idempotent — marking twice cannot produce
    two rows and inflate a progress count.
    """

    __tablename__ = "course_lesson_completions"
    __table_args__ = (
        UniqueConstraint("user_id", "lesson_id", name="uq_lesson_completion_user_lesson"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("course_lessons.id", ondelete="CASCADE"), index=True
    )
    completed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
