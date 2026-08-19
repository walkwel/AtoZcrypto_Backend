"""Seeds the Academy curriculum into the database.

The programme is authored as typed data in `courses/curriculum` and inserted
here. Seeding is idempotent and keyed on slug: a module that already exists is
skipped entirely, including its lessons. That is deliberate — once a module is
in the database, editors own it through the admin panel, and re-running the seed
after a deploy must never resurrect the original copy over their work.

To intentionally re-seed a module, delete it in the admin panel first.
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.courses.curriculum import CURRICULUM
from app.modules.courses.models import CourseLesson, CourseModule


async def seed_courses(db: AsyncSession) -> int:
    """Insert any curriculum module that is not already present.

    Returns the number of modules inserted.
    """
    existing = set((await db.execute(select(CourseModule.slug))).scalars().all())

    inserted = 0
    for position, spec in enumerate(CURRICULUM):
        if spec.slug in existing:
            continue
        db.add(
            CourseModule(
                slug=spec.slug,
                title=spec.title,
                summary=spec.summary,
                level=spec.level,
                phase=spec.phase,
                # Position comes from the curriculum's own ordering, so the
                # reading order is defined in exactly one place.
                position=position,
                is_published=True,
                lessons=[
                    CourseLesson(
                        title=lesson.title,
                        body=lesson.body,
                        kind=lesson.kind,
                        duration_minutes=lesson.minutes,
                        position=index,
                    )
                    for index, lesson in enumerate(spec.lessons)
                ],
            )
        )
        inserted += 1

    if inserted:
        await db.commit()
    return inserted
