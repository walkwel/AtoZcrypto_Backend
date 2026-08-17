"""Seed the database with sample blog content.

Run after migrations:  python -m scripts.seed
Idempotent — safe to run multiple times.
"""

import asyncio
import logging

from app.core.database import SessionFactory
from app.core.logging import setup_logging
from app.modules.blog.seed import seed_blogs

logger = logging.getLogger(__name__)


async def main() -> None:
    setup_logging()
    async with SessionFactory() as db:
        inserted = await seed_blogs(db)
    logger.info("seed complete", extra={"blogs_inserted": inserted})


if __name__ == "__main__":
    asyncio.run(main())
