"""Course (educational content) API contracts."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, computed_field

from app.modules.courses.models import CourseLevel, CoursePhase, LessonKind


class Lesson(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    body: str
    kind: LessonKind
    duration_minutes: int


class CourseModuleDetail(BaseModel):
    """A module with its lessons, in reading order."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    summary: str
    level: CourseLevel
    phase: CoursePhase
    position: int
    is_published: bool
    lessons: list[Lesson]
    updated_at: datetime

    @computed_field  # type: ignore[prop-decorator]
    @property
    def duration_minutes(self) -> int:
        """Total reading time, summed from the lessons in this response.

        Sent rather than left to the client so every surface — the module card,
        the programme header, a future email — reports the same number.
        """
        return sum(lesson.duration_minutes for lesson in self.lessons)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def lesson_count(self) -> int:
        return len(self.lessons)


class LessonInput(BaseModel):
    title: str = Field(min_length=3, max_length=512)
    body: str = Field(min_length=3)
    kind: LessonKind = LessonKind.LESSON
    # Bounded because it feeds a total the reader plans their week around; a
    # typo'd 800-minute lesson would quietly distort the whole programme.
    duration_minutes: int = Field(default=8, ge=1, le=180)


class CourseModuleCreate(BaseModel):
    """A module and its lessons, authored in one submission.

    Lessons arrive as a list rather than through their own endpoints: an editor
    thinks in whole modules, and one atomic write means a module is never
    published half-edited.
    """

    title: str = Field(min_length=3, max_length=255)
    summary: str = Field(min_length=3, max_length=1000)
    level: CourseLevel = CourseLevel.BEGINNER
    phase: CoursePhase = CoursePhase.FOUNDATIONS
    position: int = Field(default=0, ge=0, le=999)
    is_published: bool = True
    slug: str | None = Field(default=None, max_length=255)
    lessons: list[LessonInput] = Field(default_factory=list, max_length=50)


class CourseModuleUpdate(BaseModel):
    """Partial update. Omitted fields keep their stored value; supplying
    `lessons` replaces the whole set, which is what "save this module" means."""

    title: str | None = Field(default=None, min_length=3, max_length=255)
    summary: str | None = Field(default=None, min_length=3, max_length=1000)
    level: CourseLevel | None = None
    phase: CoursePhase | None = None
    position: int | None = Field(default=None, ge=0, le=999)
    is_published: bool | None = None
    lessons: list[LessonInput] | None = Field(default=None, max_length=50)


# --- Progress -------------------------------------------------------------------


class ModuleProgress(BaseModel):
    """How far one reader has got through one module."""

    module_id: int
    slug: str
    completed_lessons: int
    total_lessons: int
    completed_minutes: int
    total_minutes: int

    @computed_field  # type: ignore[prop-decorator]
    @property
    def percent(self) -> float:
        if self.total_lessons == 0:
            return 0.0
        return round(self.completed_lessons / self.total_lessons * 100, 1)


class CourseProgress(BaseModel):
    """The reader's position in the programme as a whole.

    `completed_lesson_ids` is sent alongside the roll-ups so the Academy can
    render every tick mark from one request instead of asking per module.
    """

    completed_lesson_ids: list[int]
    completed_lessons: int
    total_lessons: int
    completed_minutes: int
    total_minutes: int
    modules: list[ModuleProgress]
    last_completed_at: datetime | None

    @computed_field  # type: ignore[prop-decorator]
    @property
    def percent(self) -> float:
        if self.total_lessons == 0:
            return 0.0
        return round(self.completed_lessons / self.total_lessons * 100, 1)


class LessonProgressUpdate(BaseModel):
    """Mark a lesson complete, or undo that."""

    completed: bool
