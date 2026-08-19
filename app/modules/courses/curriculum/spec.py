"""The shape of an authored module.

The curriculum is written as plain Python data rather than a migration or a
fixture file: it is long-form editorial content, and keeping it in typed
structures means an author gets an error at import time for a missing field
instead of a broken page at runtime.

Lesson bodies are plain text with two conventions the reader (`lesson-body.tsx`)
understands, chosen so content stays readable in the source and needs no
Markdown parser at either end:

  * a blank line starts a new paragraph;
  * a line beginning with "- " is a bullet, and consecutive bullets form a list.
"""

from dataclasses import dataclass, field

from app.modules.courses.models import CourseLevel, CoursePhase, LessonKind


@dataclass(frozen=True, slots=True)
class LessonSpec:
    """One lesson: what it is called, what it says, and how long it takes.

    `minutes` is the author's estimate of reading and working time. Module and
    programme totals are summed from these, so it is the only place the length
    of the course is stated.
    """

    title: str
    body: str
    minutes: int
    kind: LessonKind = LessonKind.LESSON


@dataclass(frozen=True, slots=True)
class ModuleSpec:
    slug: str
    title: str
    summary: str
    level: CourseLevel
    phase: CoursePhase
    lessons: list[LessonSpec] = field(default_factory=list)

    @property
    def minutes(self) -> int:
        return sum(lesson.minutes for lesson in self.lessons)


def homework(title: str, body: str, minutes: int) -> LessonSpec:
    """A module's closing exercise. Badged in the UI and never just reading."""
    return LessonSpec(title=title, body=body, minutes=minutes, kind=LessonKind.HOMEWORK)
