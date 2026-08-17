"""Liveness and readiness checks.

`/health` is a cheap liveness probe. `/health/ready` verifies the datastore
dependencies so orchestrators can gate traffic on real readiness.
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.redis import Cache, get_cache

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/ready")
async def readiness(
    db: Annotated[AsyncSession, Depends(get_db)],
    cache: Annotated[Cache, Depends(get_cache)],
) -> dict[str, object]:
    database_ok = await _check_db(db)
    redis_ok = await cache.ping()
    return {
        "status": "ok" if database_ok else "degraded",
        "dependencies": {"database": database_ok, "redis": redis_ok},
    }


async def _check_db(db: AsyncSession) -> bool:
    try:
        await db.execute(text("SELECT 1"))
        return True
    except Exception:  # noqa: BLE001
        return False
