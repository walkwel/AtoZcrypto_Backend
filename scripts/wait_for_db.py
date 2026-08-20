"""Block until the database accepts connections, or give up.

The container can start before Postgres is ready — under compose that is
covered by a healthcheck, but nothing guarantees it in production, where the
database is often a separate managed service. Without this wait, `alembic
upgrade head` fails on connect, the entrypoint aborts, and the API never
starts.

Usage:
    python -m scripts.wait_for_db [timeout_seconds]
"""

import asyncio
import sys

from sqlalchemy import text

from app.core.database import engine

DEFAULT_TIMEOUT_SECONDS = 60
RETRY_DELAY_SECONDS = 2


async def wait_for_db(timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS) -> bool:
    """Poll the database until it answers, returning False if the timeout expires."""
    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout_seconds
    attempt = 0

    while True:
        attempt += 1
        try:
            async with engine.connect() as connection:
                await connection.execute(text("SELECT 1"))
            print(f"Database is ready (attempt {attempt}).")
            return True
        except Exception as exc:  # noqa: BLE001 — any connection failure is a retry
            if loop.time() >= deadline:
                print(f"Database still unreachable after {timeout_seconds}s: {exc}")
                return False
            print(f"Database not ready (attempt {attempt}), retrying in {RETRY_DELAY_SECONDS}s...")
            await asyncio.sleep(RETRY_DELAY_SECONDS)


def main() -> None:
    timeout = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_TIMEOUT_SECONDS
    if not asyncio.run(wait_for_db(timeout)):
        sys.exit(1)


if __name__ == "__main__":
    main()
