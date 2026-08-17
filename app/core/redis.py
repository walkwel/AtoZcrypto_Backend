"""Cache abstraction with two implementations.

`Cache` is the interface the whole app depends on. `RedisCache` is the real,
best-effort Redis client: if Redis is down, callers simply see a cache miss —
failures are logged, never raised. `NullCache` is a no-op used when no
`REDIS_URL` is configured, so the app runs correctly (just without caching) on
a machine that has no Redis at all.
"""

import contextlib
import json
import logging
from abc import ABC, abstractmethod
from typing import Any

from redis.asyncio import Redis

from app.core.config import get_settings

logger = logging.getLogger(__name__)


class Cache(ABC):
    """Cache interface. Services and dependencies type against this."""

    @abstractmethod
    async def get_json(self, key: str) -> Any | None: ...

    @abstractmethod
    async def set_json(self, key: str, value: Any, ttl_seconds: int) -> None: ...

    @abstractmethod
    async def delete(self, *keys: str) -> None: ...

    @abstractmethod
    async def ping(self) -> bool: ...

    async def close(self) -> None:
        return None


class RedisCache(Cache):
    def __init__(self, client: Redis) -> None:
        self._client = client

    async def get_json(self, key: str) -> Any | None:
        try:
            raw = await self._client.get(key)
        except Exception as exc:  # noqa: BLE001 — degrade gracefully on any Redis failure
            logger.warning("cache get failed", extra={"key": key, "error": str(exc)})
            return None
        return json.loads(raw) if raw is not None else None

    async def set_json(self, key: str, value: Any, ttl_seconds: int) -> None:
        try:
            await self._client.set(key, json.dumps(value, default=str), ex=ttl_seconds)
        except Exception as exc:  # noqa: BLE001
            logger.warning("cache set failed", extra={"key": key, "error": str(exc)})

    async def delete(self, *keys: str) -> None:
        try:
            if keys:
                await self._client.delete(*keys)
        except Exception as exc:  # noqa: BLE001
            logger.warning("cache delete failed", extra={"keys": keys, "error": str(exc)})

    async def ping(self) -> bool:
        try:
            return bool(await self._client.ping())
        except Exception:  # noqa: BLE001
            return False

    async def close(self) -> None:
        with contextlib.suppress(Exception):
            await self._client.aclose()


class NullCache(Cache):
    """No-op cache for environments without Redis. Every read is a miss."""

    async def get_json(self, key: str) -> Any | None:
        return None

    async def set_json(self, key: str, value: Any, ttl_seconds: int) -> None:
        return None

    async def delete(self, *keys: str) -> None:
        return None

    async def ping(self) -> bool:
        return False


_cache: Cache | None = None


def init_cache() -> Cache:
    """Build the process-wide cache from config.

    An empty REDIS_URL selects NullCache, so the app runs without Redis.
    """
    global _cache
    redis_url = get_settings().redis_url.strip()
    if not redis_url:
        logger.info("REDIS_URL not set — running without cache (NullCache)")
        _cache = NullCache()
    else:
        client = Redis.from_url(
            redis_url,
            decode_responses=True,
            socket_connect_timeout=2,
            socket_timeout=2,
        )
        _cache = RedisCache(client)
    return _cache


def get_cache() -> Cache:
    """FastAPI dependency returning the process-wide cache."""
    if _cache is None:
        raise RuntimeError("Cache not initialised — init_cache() must run at startup")
    return _cache
