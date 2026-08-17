"""Shared async HTTP client for outbound provider calls.

One connection-pooled client for the whole process, created at startup and
closed at shutdown. `request_json` adds latency logging and normalises
transport/HTTP errors into ExternalServiceError.
"""

import logging
import time
from typing import Any

import httpx

from app.core.exceptions import ExternalServiceError

logger = logging.getLogger(__name__)

_client: httpx.AsyncClient | None = None


def init_http_client() -> httpx.AsyncClient:
    global _client
    _client = httpx.AsyncClient(timeout=httpx.Timeout(15.0, connect=5.0))
    return _client


async def close_http_client() -> None:
    global _client
    if _client is not None:
        await _client.aclose()
        _client = None


def get_http_client() -> httpx.AsyncClient:
    if _client is None:
        raise RuntimeError("HTTP client not initialised — init_http_client() must run at startup")
    return _client


async def request_json(
    url: str,
    *,
    params: dict[str, Any] | None = None,
    provider: str = "unknown",
) -> Any:
    response = await _request(url, params=params, provider=provider, headers=None)
    return response.json()


async def request_text(
    url: str,
    *,
    params: dict[str, Any] | None = None,
    provider: str = "unknown",
    headers: dict[str, str] | None = None,
) -> str:
    """Fetch a text body (RSS/XML). Same error and latency contract as request_json."""
    response = await _request(url, params=params, provider=provider, headers=headers)
    return response.text


async def _request(
    url: str,
    *,
    params: dict[str, Any] | None,
    provider: str,
    headers: dict[str, str] | None,
) -> httpx.Response:
    client = get_http_client()
    started = time.perf_counter()
    try:
        # Feeds commonly redirect (e.g. to a canonical host), so follow them.
        response = await client.get(url, params=params, headers=headers, follow_redirects=True)
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        _log_latency(provider, url, started, status=exc.response.status_code)
        raise ExternalServiceError(f"{provider} returned HTTP {exc.response.status_code}") from exc
    except httpx.HTTPError as exc:
        _log_latency(provider, url, started, status=None)
        raise ExternalServiceError(f"{provider} request failed") from exc

    _log_latency(provider, url, started, status=response.status_code)
    return response


def _log_latency(provider: str, url: str, started: float, status: int | None) -> None:
    logger.info(
        "provider request",
        extra={
            "provider": provider,
            "url": url,
            "status": status,
            "latency_ms": round((time.perf_counter() - started) * 1000, 1),
        },
    )
