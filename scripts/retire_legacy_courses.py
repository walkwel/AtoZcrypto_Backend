"""Remove the three FAQ modules the Academy shipped with before the curriculum.

The Academy originally carried three short question-and-answer modules. The
fifteen-module curriculum supersedes them, but the seed is keyed on slug and so
leaves them in place — a database seeded before the curriculum landed ends up
showing both.

This is deliberately a separate, opt-in script rather than part of a migration:
an editor may have rewritten those modules through the admin panel, and a
migration that silently deleted their work would be unrecoverable.

    python -m scripts.retire_legacy_courses          # dry run, lists what would go
    python -m scripts.retire_legacy_courses --apply  # actually delete

Deleting a module takes its lessons and any progress recorded against them.
"""

import argparse
import asyncio
import logging

from sqlalchemy import select

from app.core.database import SessionFactory
from app.core.logging import setup_logging
from app.modules.courses.models import CourseModule

logger = logging.getLogger(__name__)

# The exact slugs of the original seed. Anything an editor has created since is
# untouched, because only these three are ever considered.
LEGACY_SLUGS = ["foundations", "value-and-use", "getting-started"]


async def main(apply: bool) -> None:
    setup_logging()

    async with SessionFactory() as db:
        modules = list(
            (
                await db.execute(select(CourseModule).where(CourseModule.slug.in_(LEGACY_SLUGS)))
            )
            .scalars()
            .all()
        )

        if not modules:
            logger.info("nothing to retire", extra={"slugs": LEGACY_SLUGS})
            return

        for module in modules:
            logger.info(
                "legacy module found",
                extra={
                    "slug": module.slug,
                    "title": module.title,
                    "lessons": len(module.lessons),
                    "action": "delete" if apply else "dry-run",
                },
            )

        if not apply:
            logger.info("dry run — re-run with --apply to delete", extra={"count": len(modules)})
            return

        for module in modules:
            await db.delete(module)
        await db.commit()
        logger.info("legacy modules retired", extra={"count": len(modules)})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="perform the deletion")
    asyncio.run(main(parser.parse_args().apply))
