"""Seed the database with starter blog and Academy content.

Run after migrations:  python -m scripts.seed
Idempotent — safe to run multiple times.
"""

import asyncio
import logging

from app.core.database import SessionFactory
from app.core.logging import setup_logging
from app.modules.blog.seed import seed_blogs
from app.modules.courses.seed import seed_courses

logger = logging.getLogger(__name__)


async def main() -> None:
    setup_logging()
    async with SessionFactory() as db:
        blogs = await seed_blogs(db)
        courses = await seed_courses(db)
    logger.info("seed complete", extra={"blogs_inserted": blogs, "courses_inserted": courses})


if __name__ == "__main__":
    asyncio.run(main())
