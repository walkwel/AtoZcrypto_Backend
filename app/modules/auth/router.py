"""Authentication endpoints.

REST shape: `/auth` is a collection of actions on the *session*, so the verbs
are POSTs on nouns (`/auth/login`, `/auth/refresh`) rather than RPC-ish names.
Status codes follow convention — 201 for a created account, 204 for actions
with no body, 202 for "accepted, result intentionally not disclosed".
"""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.core.config import Settings, get_settings
from app.modules.auth.dependencies import AuthServiceDep, CurrentUser
from app.modules.auth.schemas import (
    AuthResponse,
    ForgotPasswordRequest,
    ForgotPasswordResponse,
    LoginRequest,
    RefreshRequest,
    RegisterRequest,
    ResetPasswordRequest,
    UserProfile,
)

router = APIRouter(prefix="/auth", tags=["auth"])

RESET_REQUESTED_MESSAGE = (
    "If an account exists for that email, a password reset link has been sent."
)


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest, service: AuthServiceDep) -> AuthResponse:
    """Create an account and sign the new user in."""
    return await service.register(payload)


@router.post("/login", response_model=AuthResponse)
async def login(payload: LoginRequest, service: AuthServiceDep) -> AuthResponse:
    return await service.login(payload)


@router.post("/refresh", response_model=AuthResponse)
async def refresh(payload: RefreshRequest, service: AuthServiceDep) -> AuthResponse:
    """Exchange a refresh token for a new token pair (the old one is revoked)."""
    return await service.refresh(payload.refresh_token)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(payload: RefreshRequest, service: AuthServiceDep) -> None:
    await service.logout(payload.refresh_token)


@router.get("/me", response_model=UserProfile)
async def me(user: CurrentUser, service: AuthServiceDep) -> UserProfile:
    return await service.get_profile(user.user_id)


@router.post(
    "/forgot-password",
    response_model=ForgotPasswordResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
async def forgot_password(
    payload: ForgotPasswordRequest,
    service: AuthServiceDep,
    settings: Annotated[Settings, Depends(get_settings)],
) -> ForgotPasswordResponse:
    """Always returns 202 with the same message, so the response can't be used
    to discover which emails have accounts."""
    token = await service.request_password_reset(payload.email)
    return ForgotPasswordResponse(
        message=RESET_REQUESTED_MESSAGE,
        # No mail service in V1: outside production the token is returned so the
        # flow is usable locally. Never disclosed in production.
        reset_token=None if settings.is_production else token,
    )


@router.post("/reset-password", status_code=status.HTTP_204_NO_CONTENT)
async def reset_password(payload: ResetPasswordRequest, service: AuthServiceDep) -> None:
    await service.reset_password(payload.token, payload.password)
