"""FastAPI wiring and route guards for authentication.

`CurrentUser` / `AdminUser` are the two guards the rest of the app uses:

    async def endpoint(user: CurrentUser) -> ...:   # any signed-in account
    async def endpoint(user: AdminUser) -> ...:     # role == admin

Both verify the JWT signature locally — no database round-trip — and only the
claims are trusted. Endpoints never parse the Authorization header themselves.
"""

from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.core.database import get_db
from app.core.exceptions import ForbiddenError, UnauthorizedError
from app.modules.auth.models import UserRole
from app.modules.auth.repository import AuthRepository
from app.modules.auth.security import InvalidTokenError, TokenClaims, decode_access_token
from app.modules.auth.service import AuthService

# auto_error=False so a missing header raises our own 401 envelope, not FastAPI's.
bearer_scheme = HTTPBearer(auto_error=False)


def get_auth_service(
    db: Annotated[AsyncSession, Depends(get_db)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> AuthService:
    return AuthService(AuthRepository(db), settings)


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]


def get_current_claims(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> TokenClaims:
    if credentials is None:
        raise UnauthorizedError("Authentication required.")
    try:
        return decode_access_token(credentials.credentials, settings=settings)
    except InvalidTokenError as exc:
        raise UnauthorizedError("Invalid or expired access token.") from exc


CurrentUser = Annotated[TokenClaims, Depends(get_current_claims)]


def get_optional_claims(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> TokenClaims | None:
    """Identity when it is offered, anonymity when it is not.

    For endpoints that everyone may call but that are richer for a known user —
    feedback is linked to an account when one is signed in. A malformed or
    expired token is treated as absent rather than rejected: the caller was not
    required to prove anything, so a bad optional credential must not turn a
    valid request into a 401.
    """
    if credentials is None:
        return None
    try:
        return decode_access_token(credentials.credentials, settings=settings)
    except InvalidTokenError:
        return None


OptionalUser = Annotated[TokenClaims | None, Depends(get_optional_claims)]


def get_current_admin(claims: CurrentUser) -> TokenClaims:
    if claims.role != UserRole.ADMIN:
        raise ForbiddenError("This action requires an administrator account.")
    return claims


AdminUser = Annotated[TokenClaims, Depends(get_current_admin)]

# Use in `dependencies=[...]` when the endpoint doesn't need the identity itself.
RequireAdmin = Depends(get_current_admin)
