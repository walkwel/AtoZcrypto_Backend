"""Request middleware: assign a request ID, log each request's outcome, and
catch unhandled exceptions where CORS headers still apply.
"""

import logging
import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from app.core.exceptions import error_response
from app.core.logging import request_id_ctx

logger = logging.getLogger("app.request")
error_logger = logging.getLogger(__name__)


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """Turns an unhandled exception into the standard JSON error envelope.

    Must be added to the app *before* CORSMiddleware (see main.py) so it ends
    up inside it: Starlette runs `@app.exception_handler(Exception)` via
    ServerErrorMiddleware, which sits outside CORSMiddleware, so that path
    never gets CORS headers and the browser reports "blocked by CORS policy"
    instead of the real 500. Catching the exception here lets the response
    flow back out through CORSMiddleware like any other response.
    """

    async def dispatch(self, request: Request, call_next) -> Response:  # type: ignore[no-untyped-def]
        try:
            return await call_next(request)
        except Exception:
            error_logger.exception("unhandled error", extra={"path": request.url.path})
            return error_response(
                HTTP_500_INTERNAL_SERVER_ERROR,
                "internal_error",
                "An unexpected error occurred.",
            )


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:  # type: ignore[no-untyped-def]
        request_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex
        token = request_id_ctx.set(request_id)
        started = time.perf_counter()
        try:
            response = await call_next(request)
        finally:
            request_id_ctx.reset(token)

        duration_ms = round((time.perf_counter() - started) * 1000, 1)
        logger.info(
            "request handled",
            extra={
                "method": request.method,
                "path": request.url.path,
                "status": response.status_code,
                "duration_ms": duration_ms,
            },
        )
        response.headers["X-Request-ID"] = request_id
        return response
