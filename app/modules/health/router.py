"""Liveness and readiness checks.

`/health` is a cheap liveness probe. `/health/ready` verifies the datastore
dependencies so orchestrators can gate traffic on real readiness.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
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
    response: Response,
    db: Annotated[AsyncSession, Depends(get_db)],
    cache: Annotated[Cache, Depends(get_cache)],
) -> dict[str, object]:
    """Readiness for orchestrators and deploy checks.

    The status *code* carries the verdict, not just the body: probes and load
    balancers route on the code alone, so answering 200 while reporting
    "degraded" would keep traffic flowing to an instance that cannot serve it.

    Redis is deliberately not part of that verdict. The cache degrades to a
    miss when it is unavailable (see core/redis.py), so the app is still ready
    without it — its state is reported for visibility only.
    """
    database_ok = await _check_db(db)
    redis_ok = await cache.ping()

    if not database_ok:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

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
