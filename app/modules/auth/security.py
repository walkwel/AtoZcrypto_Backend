"""Password hashing and JWT encode/decode.

Pure functions with no DB or HTTP concerns, so they are trivial to unit test.

Two different token families live here:

* **JWTs** (access tokens) — stateless, signed, short-lived. Verified by
  signature alone; no database round-trip on every request.
* **Opaque tokens** (refresh, password reset) — random strings handed to the
  client, stored server-side only as SHA-256 hashes so a database leak cannot
  be replayed. They are revocable, which is exactly why they are not JWTs.
"""

import hashlib
import secrets
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Any, Literal

import bcrypt
import jwt

from app.core.config import Settings

TokenType = Literal["access", "refresh"]

# bcrypt truncates silently beyond 72 bytes; reject instead of hashing a prefix.
MAX_PASSWORD_BYTES = 72


class InvalidTokenError(Exception):
    """Raised when a JWT is malformed, expired, or of the wrong type."""


@dataclass(slots=True)
class TokenClaims:
    user_id: int
    email: str
    role: str


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode(), password_hash.encode())
    except ValueError:
        # Malformed hash in the database — treat as a failed login, never a 500.
        return False


def create_access_token(*, user_id: int, email: str, role: str, settings: Settings) -> str:
    now = datetime.now(UTC)
    payload: dict[str, Any] = {
        "sub": str(user_id),
        "email": email,
        "role": role,
        "type": "access",
        "iat": now,
        "exp": now + timedelta(minutes=settings.access_token_expire_minutes),
        "jti": uuid.uuid4().hex,
    }
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str, *, settings: Settings) -> TokenClaims:
    """Verify signature/expiry and return the caller's identity."""
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
            options={"require": ["exp", "sub"]},
        )
    except jwt.PyJWTError as exc:
        raise InvalidTokenError(str(exc)) from exc

    if payload.get("type") != "access":
        raise InvalidTokenError("Not an access token.")

    try:
        user_id = int(payload["sub"])
    except (KeyError, TypeError, ValueError) as exc:
        raise InvalidTokenError("Token subject is not a user id.") from exc

    return TokenClaims(
        user_id=user_id,
        email=payload.get("email", ""),
        role=payload.get("role", ""),
    )


def generate_opaque_token() -> str:
    """A high-entropy token handed to the client (refresh / password reset)."""
    return secrets.token_urlsafe(48)


def hash_opaque_token(token: str) -> str:
    """SHA-256 of an opaque token — what we store and look up by.

    A plain hash (no salt/stretching) is correct here: unlike passwords, these
    tokens are already 384 bits of entropy, so they are not brute-forceable.
    """
    return hashlib.sha256(token.encode()).hexdigest()
