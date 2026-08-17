"""Minimal in-process periodic task runner.

This is intentionally small. It exists so news refresh can run on a schedule
without pulling in Celery or a message broker for V1. The refresh *logic* lives
in NewsService, so migrating this loop to Celery / Cloud Scheduler later means
replacing this file only — no business-logic changes.
"""

import asyncio
import contextlib
import logging
from collections.abc import Awaitable, Callable

logger = logging.getLogger(__name__)


class PeriodicScheduler:
    def __init__(self) -> None:
        self._tasks: list[asyncio.Task] = []

    def schedule(
        self,
        job: Callable[[], Awaitable[None]],
        *,
        interval_seconds: int,
        name: str,
        run_immediately: bool = True,
    ) -> None:
        self._tasks.append(
            asyncio.create_task(
                self._run_loop(job, interval_seconds, name, run_immediately), name=name
            )
        )

    async def _run_loop(
        self,
        job: Callable[[], Awaitable[None]],
        interval_seconds: int,
        name: str,
        run_immediately: bool,
    ) -> None:
        if not run_immediately:
            await asyncio.sleep(interval_seconds)
        while True:
            try:
                await job()
            except asyncio.CancelledError:
                raise
            except Exception:  # noqa: BLE001 — one failed run must not kill the loop
                logger.exception("scheduled job failed", extra={"job": name})
            await asyncio.sleep(interval_seconds)

    async def shutdown(self) -> None:
        for task in self._tasks:
            task.cancel()
        for task in self._tasks:
            with contextlib.suppress(asyncio.CancelledError):
                await task
        self._tasks.clear()
