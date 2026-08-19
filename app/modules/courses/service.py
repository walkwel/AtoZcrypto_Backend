"""Educational content business logic.

Reads are cached: the Academy page is read constantly and written rarely, and
every write invalidates the cache so an editor sees their change immediately
rather than some time within the TTL.

Progress is deliberately *not* cached. It is per-user, changes on every lesson a
reader finishes, and is read once per page load — a cache here would serve stale
tick marks in exchange for nothing.
"""

import logging
from datetime import datetime

from app.core.config import Settings
from app.core.exceptions import ConflictError, NotFoundError
from app.core.redis import Cache
from app.modules.blog.slug import slugify
from app.modules.courses.models import CourseLesson, CourseModule
from app.modules.courses.repository import CourseRepository, ProgressRepository
from app.modules.courses.schemas import (
    CourseModuleCreate,
    CourseModuleDetail,
    CourseModuleUpdate,
    CourseProgress,
    LessonInput,
    ModuleProgress,
)

logger = logging.getLogger(__name__)

_PUBLISHED_KEY = "courses:published"


class CourseService:
    def __init__(self, repository: CourseRepository, cache: Cache, settings: Settings) -> None:
        self._repository = repository
        self._cache = cache
        self._ttl = settings.blog_cache_ttl

    async def list_modules(self, *, include_unpublished: bool = False) -> list[CourseModuleDetail]:
        # Only the public view is cached; the admin list must always show the
        # true current state, drafts included.
        if include_unpublished:
            modules = await self._repository.list_modules(published_only=False)
            return [CourseModuleDetail.model_validate(module) for module in modules]

        cached = await self._cache.get_json(_PUBLISHED_KEY)
        if cached is not None:
            return [CourseModuleDetail.model_validate(item) for item in cached]

        modules = await self._repository.list_modules(published_only=True)
        payload = [CourseModuleDetail.model_validate(module) for module in modules]
        await self._cache.set_json(
            _PUBLISHED_KEY, [item.model_dump(mode="json") for item in payload], self._ttl
        )
        return payload

    async def get_module(self, slug: str) -> CourseModuleDetail:
        return CourseModuleDetail.model_validate(await self._require(slug))

    async def create_module(self, payload: CourseModuleCreate) -> CourseModuleDetail:
        slug = await self._unique_slug(payload.slug or payload.title)
        module = CourseModule(
            slug=slug,
            title=payload.title,
            summary=payload.summary,
            level=payload.level,
            phase=payload.phase,
            position=payload.position or await self._repository.next_position(),
            is_published=payload.is_published,
            lessons=_to_lessons(payload.lessons),
        )
        created = await self._repository.add(module)
        await self._invalidate()
        logger.info("course module created", extra={"slug": slug})
        return CourseModuleDetail.model_validate(created)

    async def update_module(self, slug: str, payload: CourseModuleUpdate) -> CourseModuleDetail:
        module = await self._require(slug)

        for field, value in payload.model_dump(exclude_unset=True, exclude={"lessons"}).items():
            setattr(module, field, value)

        if payload.lessons is not None:
            # Replace rather than merge: the editor submits the module as it
            # should now read, so deletions and reordering are expressed simply
            # by what is (and is not) in the list.
            module.lessons = _to_lessons(payload.lessons)

        await self._repository.save(module)
        await self._invalidate()
        return CourseModuleDetail.model_validate(module)

    async def delete_module(self, slug: str) -> None:
        await self._repository.delete(await self._require(slug))
        await self._invalidate()

    async def count(self) -> int:
        return await self._repository.count()

    async def _require(self, slug: str) -> CourseModule:
        module = await self._repository.get_by_slug(slug)
        if module is None:
            raise NotFoundError("Course module not found.")
        return module

    async def _unique_slug(self, source: str) -> str:
        slug = slugify(source)[:255]
        if not slug:
            raise ConflictError("Could not derive a slug from that title.")
        if await self._repository.slug_exists(slug):
            raise ConflictError("A module with that title already exists.")
        return slug

    async def _invalidate(self) -> None:
        await self._cache.delete(_PUBLISHED_KEY)


class ProgressService:
    """A reader's way through the curriculum.

    Progress is always reported against the *published* curriculum. A completion
    for a lesson that has since been unpublished stays in the database — the
    reader really did read it, and republishing the module should restore their
    tick — but it is left out of the totals so a percentage can never exceed
    what is currently on offer.
    """

    def __init__(self, courses: CourseRepository, progress: ProgressRepository) -> None:
        self._courses = courses
        self._progress = progress

    async def for_user(self, user_id: int) -> CourseProgress:
        modules = await self._courses.list_modules(published_only=True)
        completed = await self._progress.completed_lesson_ids(user_id)

        module_progress: list[ModuleProgress] = []
        completed_lessons = total_lessons = 0
        completed_minutes = total_minutes = 0
        published_lesson_ids: set[int] = set()

        for module in modules:
            done = [lesson for lesson in module.lessons if lesson.id in completed]
            module_minutes = sum(lesson.duration_minutes for lesson in module.lessons)
            done_minutes = sum(lesson.duration_minutes for lesson in done)
            published_lesson_ids.update(lesson.id for lesson in module.lessons)

            module_progress.append(
                ModuleProgress(
                    module_id=module.id,
                    slug=module.slug,
                    completed_lessons=len(done),
                    total_lessons=len(module.lessons),
                    completed_minutes=done_minutes,
                    total_minutes=module_minutes,
                )
            )

            completed_lessons += len(done)
            total_lessons += len(module.lessons)
            completed_minutes += done_minutes
            total_minutes += module_minutes

        return CourseProgress(
            completed_lesson_ids=sorted(completed & published_lesson_ids),
            completed_lessons=completed_lessons,
            total_lessons=total_lessons,
            completed_minutes=completed_minutes,
            total_minutes=total_minutes,
            modules=module_progress,
            last_completed_at=await self._last_completed_at(user_id),
        )

    async def set_lesson(self, user_id: int, lesson_id: int, *, completed: bool) -> CourseProgress:
        lesson = await self._courses.get_lesson(lesson_id)
        if lesson is None:
            raise NotFoundError("Lesson not found.")

        if completed:
            await self._progress.mark_complete(user_id, lesson_id)
        else:
            await self._progress.mark_incomplete(user_id, lesson_id)

        # Return the whole picture rather than an acknowledgement: one round trip
        # updates the lesson's tick, its module bar, and the overall ring.
        return await self.for_user(user_id)

    async def reset(self, user_id: int) -> CourseProgress:
        await self._progress.reset(user_id)
        return await self.for_user(user_id)

    async def _last_completed_at(self, user_id: int) -> datetime | None:
        return await self._progress.last_completed_at(user_id)


def _to_lessons(lessons: list[LessonInput]) -> list[CourseLesson]:
    """Position follows list order — the order the editor chose is the truth."""
    return [
        CourseLesson(
            title=lesson.title,
            body=lesson.body,
            kind=lesson.kind,
            duration_minutes=lesson.duration_minutes,
            position=index,
        )
        for index, lesson in enumerate(lessons)
    ]
