"""Authentication business logic.

Security properties this service is responsible for:

* Passwords are only ever persisted as bcrypt hashes.
* Login failures are indistinguishable from "no such user" (no enumeration),
  and forgot-password always responds identically for the same reason.
* Refresh tokens are **rotated**: using one revokes it and issues a new pair.
  Re-using an already-revoked token revokes the user's whole session family,
  which is the standard response to a suspected token theft.
* Resetting a password revokes every outstanding refresh token.
"""

import logging
from datetime import UTC, datetime, timedelta

from app.core.config import Settings
from app.core.exceptions import ConflictError, UnauthorizedError
from app.modules.auth.models import PasswordResetToken, RefreshToken, User, UserRole
from app.modules.auth.repository import AuthRepository
from app.modules.auth.schemas import (
    AuthResponse,
    LoginRequest,
    RegisterRequest,
    TokenPair,
    UserProfile,
)
from app.modules.auth.security import (
    create_access_token,
    generate_opaque_token,
    hash_opaque_token,
    hash_password,
    verify_password,
)

logger = logging.getLogger(__name__)

INVALID_CREDENTIALS = "Incorrect email or password."
INVALID_REFRESH = "Invalid or expired refresh token."
INVALID_RESET = "This password reset link is invalid or has expired."


class AuthService:
    def __init__(self, repository: AuthRepository, settings: Settings) -> None:
        self._repo = repository
        self._settings = settings

    # --- registration & login -------------------------------------------------

    async def register(self, data: RegisterRequest) -> AuthResponse:
        email = self._normalize_email(data.email)
        if await self._repo.get_user_by_email(email) is not None:
            raise ConflictError("An account with this email already exists.")

        user = await self._repo.add_user(
            User(
                email=email,
                password_hash=hash_password(data.password),
                full_name=data.full_name.strip(),
                role=UserRole.USER,
            )
        )
        logger.info("user registered", extra={"user_id": user.id})
        return await self._authenticated_response(user)

    async def login(self, data: LoginRequest) -> AuthResponse:
        user = await self._repo.get_user_by_email(self._normalize_email(data.email))

        # Always verify against *something* so the response time doesn't reveal
        # whether the account exists.
        password_hash = user.password_hash if user else _DUMMY_HASH
        password_ok = verify_password(data.password, password_hash)

        if user is None or not password_ok:
            raise UnauthorizedError(INVALID_CREDENTIALS)
        if not user.is_active:
            raise UnauthorizedError("This account has been deactivated.")

        return await self._authenticated_response(user)

    # --- session lifecycle ----------------------------------------------------

    async def refresh(self, refresh_token: str) -> AuthResponse:
        stored = await self._repo.get_refresh_token(hash_opaque_token(refresh_token))
        if stored is None:
            raise UnauthorizedError(INVALID_REFRESH)

        now = datetime.now(UTC)
        if stored.revoked_at is not None:
            # A revoked token being presented means it leaked (or was replayed).
            # Kill every session for that user rather than just rejecting this one.
            logger.warning("refresh token reuse detected", extra={"user_id": stored.user_id})
            await self._repo.revoke_all_refresh_tokens(stored.user_id, at=now)
            raise UnauthorizedError(INVALID_REFRESH)
        if _as_utc(stored.expires_at) <= now:
            raise UnauthorizedError(INVALID_REFRESH)

        user = await self._repo.get_user_by_id(stored.user_id)
        if user is None or not user.is_active:
            raise UnauthorizedError(INVALID_REFRESH)

        await self._repo.revoke_refresh_token(stored, at=now)
        return await self._authenticated_response(user)

    async def logout(self, refresh_token: str) -> None:
        """Revoke the presented refresh token. Idempotent by design: logging out
        twice, or with an unknown token, is still a success for the caller."""
        stored = await self._repo.get_refresh_token(hash_opaque_token(refresh_token))
        if stored is not None and stored.revoked_at is None:
            await self._repo.revoke_refresh_token(stored, at=datetime.now(UTC))

    # --- password reset -------------------------------------------------------

    async def request_password_reset(self, email: str) -> str | None:
        """Issue a reset token. Returns it so non-production callers can surface
        it; production would email it instead. Unknown emails return None and
        the router responds identically either way."""
        user = await self._repo.get_user_by_email(self._normalize_email(email))
        if user is None or not user.is_active:
            logger.info("password reset requested for unknown or inactive account")
            return None

        token = generate_opaque_token()
        await self._repo.add_reset_token(
            PasswordResetToken(
                user_id=user.id,
                token_hash=hash_opaque_token(token),
                expires_at=datetime.now(UTC)
                + timedelta(minutes=self._settings.password_reset_token_expire_minutes),
            )
        )
        logger.info("password reset token issued", extra={"user_id": user.id})
        return token

    async def reset_password(self, token: str, new_password: str) -> None:
        stored = await self._repo.get_reset_token(hash_opaque_token(token))
        now = datetime.now(UTC)
        if stored is None or stored.used_at is not None or _as_utc(stored.expires_at) <= now:
            raise UnauthorizedError(INVALID_RESET)

        user = await self._repo.get_user_by_id(stored.user_id)
        if user is None or not user.is_active:
            raise UnauthorizedError(INVALID_RESET)

        user.password_hash = hash_password(new_password)
        stored.used_at = now
        await self._repo.save()

        # A password change must invalidate sessions created with the old one.
        await self._repo.revoke_all_refresh_tokens(user.id, at=now)
        logger.info("password reset completed", extra={"user_id": user.id})

    # --- helpers --------------------------------------------------------------

    async def get_profile(self, user_id: int) -> UserProfile:
        user = await self._repo.get_user_by_id(user_id)
        if user is None or not user.is_active:
            raise UnauthorizedError("Account is no longer available.")
        return UserProfile.model_validate(user)

    async def _authenticated_response(self, user: User) -> AuthResponse:
        return AuthResponse(
            user=UserProfile.model_validate(user),
            tokens=await self._issue_tokens(user),
        )

    async def _issue_tokens(self, user: User) -> TokenPair:
        refresh_token = generate_opaque_token()
        await self._repo.add_refresh_token(
            RefreshToken(
                user_id=user.id,
                token_hash=hash_opaque_token(refresh_token),
                expires_at=datetime.now(UTC)
                + timedelta(days=self._settings.refresh_token_expire_days),
            )
        )
        access_token = create_access_token(
            user_id=user.id, email=user.email, role=user.role, settings=self._settings
        )
        return TokenPair(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=self._settings.access_token_expire_minutes * 60,
        )

    @staticmethod
    def _normalize_email(email: str) -> str:
        return email.strip().lower()


def _as_utc(value: datetime) -> datetime:
    """SQLite returns naive datetimes; normalise before comparing."""
    return value if value.tzinfo else value.replace(tzinfo=UTC)


# Hashing a throwaway password keeps failed-login timing similar to a real one.
_DUMMY_HASH = hash_password("not-a-real-password-000")
