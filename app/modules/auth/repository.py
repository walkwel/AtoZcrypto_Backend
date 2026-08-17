"""Database access for users and their tokens."""

from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.models import PasswordResetToken, RefreshToken, User


class AuthRepository:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    # --- users ---------------------------------------------------------------

    async def get_user_by_email(self, email: str) -> User | None:
        return await self._db.scalar(select(User).where(User.email == email))

    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self._db.scalar(select(User).where(User.id == user_id))

    async def add_user(self, user: User) -> User:
        self._db.add(user)
        await self._db.commit()
        await self._db.refresh(user)
        return user

    async def save(self) -> None:
        await self._db.commit()

    # --- refresh tokens ------------------------------------------------------

    async def add_refresh_token(self, token: RefreshToken) -> RefreshToken:
        self._db.add(token)
        await self._db.commit()
        return token

    async def get_refresh_token(self, token_hash: str) -> RefreshToken | None:
        return await self._db.scalar(
            select(RefreshToken).where(RefreshToken.token_hash == token_hash)
        )

    async def revoke_refresh_token(self, token: RefreshToken, *, at: datetime) -> None:
        token.revoked_at = at
        await self._db.commit()

    async def revoke_all_refresh_tokens(self, user_id: int, *, at: datetime) -> None:
        """Used on password reset so existing sessions cannot outlive it."""
        await self._db.execute(
            update(RefreshToken)
            .where(RefreshToken.user_id == user_id, RefreshToken.revoked_at.is_(None))
            .values(revoked_at=at)
        )
        await self._db.commit()

    # --- password reset tokens ----------------------------------------------

    async def add_reset_token(self, token: PasswordResetToken) -> PasswordResetToken:
        self._db.add(token)
        await self._db.commit()
        return token

    async def get_reset_token(self, token_hash: str) -> PasswordResetToken | None:
        return await self._db.scalar(
            select(PasswordResetToken).where(PasswordResetToken.token_hash == token_hash)
        )
