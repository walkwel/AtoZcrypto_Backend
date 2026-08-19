"""Application errors and their HTTP mapping.

Handlers return a consistent error envelope and never leak stack traces
or internal details to clients.
"""

import logging

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)


class AppError(Exception):
    """Base class for expected application errors."""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    code = "internal_error"

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class NotFoundError(AppError):
    status_code = status.HTTP_404_NOT_FOUND
    code = "not_found"


class UnauthorizedError(AppError):
    """Missing, invalid, or expired credentials."""

    status_code = status.HTTP_401_UNAUTHORIZED
    code = "unauthorized"


class ForbiddenError(AppError):
    status_code = status.HTTP_403_FORBIDDEN
    code = "forbidden"


class ConflictError(AppError):
    """The request collides with existing state (e.g. email already registered)."""

    status_code = status.HTTP_409_CONFLICT
    code = "conflict"


class ValidationError(AppError):
    status_code = status.HTTP_400_BAD_REQUEST
    code = "invalid_request"


class ExternalServiceError(AppError):
    """An upstream provider (news/market API) failed or timed out."""

    status_code = status.HTTP_502_BAD_GATEWAY
    code = "external_service_error"


def _safe_validation_details(exc: RequestValidationError) -> list[dict[str, str]]:
    """Reduce Pydantic errors to JSON-safe, non-sensitive fields.

    Pydantic's raw errors embed the rejected `input` (which for a signup would
    echo the submitted password straight back) and a `ctx` that can hold an
    exception instance, which is not JSON-serialisable. Only the field location,
    message, and error type are safe to return.
    """
    return [
        {
            "field": ".".join(str(part) for part in error.get("loc", ())),
            "message": str(error.get("msg", "")),
            "type": str(error.get("type", "")),
        }
        for error in exc.errors()
    ]


def error_response(status_code: int, code: str, message: str) -> JSONResponse:
    # RFC 6750: a 401 from a bearer-token API must advertise the scheme.
    is_unauthorized = status_code == status.HTTP_401_UNAUTHORIZED
    headers = {"WWW-Authenticate": "Bearer"} if is_unauthorized else None
    return JSONResponse(
        status_code=status_code,
        content={"error": {"code": code, "message": message}},
        headers=headers,
    )


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def handle_app_error(request: Request, exc: AppError) -> JSONResponse:
        if exc.status_code >= 500:
            logger.error("application error", extra={"code": exc.code, "detail": exc.message})
        return error_response(exc.status_code, exc.code, exc.message)

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "error": {
                    "code": "validation_error",
                    "message": "Request validation failed.",
                    "details": _safe_validation_details(exc),
                }
            },
        )

    # Fallback only: ErrorHandlingMiddleware (app/core/middleware.py) catches
    # unhandled exceptions from routes and normally handles this response
    # itself. Starlette runs base-Exception handlers via ServerErrorMiddleware,
    # which sits *outside* CORSMiddleware, so a response built here never gets
    # CORS headers — the browser reports a misleading "blocked by CORS policy"
    # instead of the real error. This stays registered only to catch the rare
    # case of an exception raised by a middleware itself, above where
    # ErrorHandlingMiddleware can see it.
    @app.exception_handler(Exception)
    async def handle_unexpected_error(request: Request, exc: Exception) -> JSONResponse:
        logger.exception("unhandled error", extra={"path": request.url.path})
        return error_response(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "internal_error",
            "An unexpected error occurred.",
        )
