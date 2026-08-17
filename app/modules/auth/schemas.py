from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.modules.auth.security import MAX_PASSWORD_BYTES

PASSWORD_MIN_LENGTH = 8


class PasswordMixin(BaseModel):
    """Shared password policy so every entry point validates identically."""

    password: str = Field(min_length=PASSWORD_MIN_LENGTH, max_length=128)

    @field_validator("password")
    @classmethod
    def validate_strength(cls, value: str) -> str:
        if len(value.encode()) > MAX_PASSWORD_BYTES:
            raise ValueError("Password is too long.")
        if not any(char.isalpha() for char in value):
            raise ValueError("Password must contain at least one letter.")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one number.")
        return value


class RegisterRequest(PasswordMixin):
    email: EmailStr
    full_name: str = Field(min_length=2, max_length=255)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)


class RefreshRequest(BaseModel):
    refresh_token: str = Field(min_length=1, max_length=512)


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(PasswordMixin):
    token: str = Field(min_length=1, max_length=512)


class UserProfile(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    full_name: str
    role: str
    created_at: datetime


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # access token lifetime in seconds


class AuthResponse(BaseModel):
    """Returned by register/login: who you are plus how to call the API."""

    user: UserProfile
    tokens: TokenPair


class ForgotPasswordResponse(BaseModel):
    """Always the same shape, whether or not the email exists (no enumeration).

    `reset_token` is populated **only outside production**, where there is no
    mail service wired up — it lets the flow be exercised end to end locally.
    """

    message: str
    reset_token: str | None = None
