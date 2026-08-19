"""Database access for educational content."""

from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.courses.models import CourseLesson, CourseModule, LessonCompletion


class CourseRepository:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def list_modules(self, *, published_only: bool = True) -> list[CourseModule]:
        """Modules in reading order, lessons eagerly loaded (see the relationship).

        The Academy shows every module on one page, so this returns the whole
        set: it is editorial content measured in dozens of rows, and paginating
        it would add a control the reader has no use for.
        """
        query = select(CourseModule)
        if published_only:
            query = query.where(CourseModule.is_published.is_(True))
        query = query.order_by(CourseModule.position, CourseModule.id)
        return list((await self._db.execute(query)).scalars().all())

    async def get_by_slug(self, slug: str) -> CourseModule | None:
        return await self._db.scalar(select(CourseModule).where(CourseModule.slug == slug))

    async def slug_exists(self, slug: str) -> bool:
        found = await self._db.scalar(select(CourseModule.id).where(CourseModule.slug == slug))
        return found is not None

    async def count(self) -> int:
        return await self._db.scalar(select(func.count(CourseModule.id))) or 0

    async def next_position(self) -> int:
        """Append new modules to the end of the running order."""
        highest = await self._db.scalar(select(func.max(CourseModule.position)))
        return int(highest) + 1 if highest is not None else 0

    async def get_lesson(self, lesson_id: int) -> CourseLesson | None:
        return await self._db.get(CourseLesson, lesson_id)

    # --- writes ---------------------------------------------------------------

    async def add(self, module: CourseModule) -> CourseModule:
        self._db.add(module)
        await self._db.commit()
        await self._db.refresh(module)
        return module

    async def save(self, module: CourseModule) -> None:
        """Commit and reload the row.

        The reload is not optional: `updated_at` is set by the database, and
        reading it back lazily during response serialisation would attempt IO
        outside the async context and fail.
        """
        await self._db.commit()
        await self._db.refresh(module)

    async def delete(self, module: CourseModule) -> None:
        await self._db.delete(module)
        await self._db.commit()


class ProgressRepository:
    """Lesson completions for one reader.

    Completions are a set, not a history: the queries here answer "which lessons
    has this user finished", and marking is idempotent so a retried request
    cannot double-count.
    """

    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def completed_lesson_ids(self, user_id: int) -> set[int]:
        rows = await self._db.execute(
            select(LessonCompletion.lesson_id).where(LessonCompletion.user_id == user_id)
        )
        return set(rows.scalars().all())

    async def last_completed_at(self, user_id: int):
        return await self._db.scalar(
            select(func.max(LessonCompletion.completed_at)).where(
                LessonCompletion.user_id == user_id
            )
        )

    async def mark_complete(self, user_id: int, lesson_id: int) -> None:
        """No-op when the lesson is already done, so re-marking is safe."""
        existing = await self._db.scalar(
            select(LessonCompletion.id).where(
                LessonCompletion.user_id == user_id,
                LessonCompletion.lesson_id == lesson_id,
            )
        )
        if existing is not None:
            return
        self._db.add(LessonCompletion(user_id=user_id, lesson_id=lesson_id))
        await self._db.commit()

    async def mark_incomplete(self, user_id: int, lesson_id: int) -> None:
        await self._db.execute(
            delete(LessonCompletion).where(
                LessonCompletion.user_id == user_id,
                LessonCompletion.lesson_id == lesson_id,
            )
        )
        await self._db.commit()

    async def reset(self, user_id: int) -> None:
        await self._db.execute(delete(LessonCompletion).where(LessonCompletion.user_id == user_id))
        await self._db.commit()
