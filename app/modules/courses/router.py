"""Course (educational content) HTTP endpoints.

Reads are public — the Academy is a marketing surface as much as a learning
one — with one exception: unpublished drafts are visible only to admins.
Authoring requires the admin role, exactly like blogs.

Progress is the mirror image: it is personal, so every progress route requires a
signed-in account and is scoped to that account's own token claims. There is no
route that reads or writes another user's progress.
"""

from typing import Annotated

from fastapi import APIRouter, Query, status

from app.core.exceptions import ForbiddenError
from app.modules.auth.dependencies import CurrentUser, OptionalUser, RequireAdmin
from app.modules.auth.models import UserRole
from app.modules.courses.dependencies import CourseServiceDep, ProgressServiceDep
from app.modules.courses.schemas import (
    CourseModuleCreate,
    CourseModuleDetail,
    CourseModuleUpdate,
    CourseProgress,
    LessonProgressUpdate,
)

router = APIRouter(prefix="/courses", tags=["courses"])


@router.get("", response_model=list[CourseModuleDetail])
async def list_courses(
    service: CourseServiceDep,
    claims: OptionalUser,
    include_unpublished: Annotated[bool, Query()] = False,
) -> list[CourseModuleDetail]:
    if include_unpublished:
        # Drafts are unpublished for a reason; asking for them is an admin
        # action even though the endpoint itself is public.
        if claims is None or claims.role != UserRole.ADMIN:
            raise ForbiddenError("Unpublished modules require an administrator account.")
        return await service.list_modules(include_unpublished=True)
    return await service.list_modules()


@router.post(
    "",
    response_model=CourseModuleDetail,
    status_code=status.HTTP_201_CREATED,
    dependencies=[RequireAdmin],
)
async def create_course(
    payload: CourseModuleCreate, service: CourseServiceDep
) -> CourseModuleDetail:
    return await service.create_module(payload)


# --- Progress -------------------------------------------------------------------
#
# Declared before `/{slug}` so "progress" is read as this route and not as the
# slug of a module someone might one day publish under that name.


@router.get("/progress", response_model=CourseProgress)
async def get_progress(claims: CurrentUser, service: ProgressServiceDep) -> CourseProgress:
    return await service.for_user(claims.user_id)


@router.put("/progress/lessons/{lesson_id}", response_model=CourseProgress)
async def set_lesson_progress(
    lesson_id: int,
    payload: LessonProgressUpdate,
    claims: CurrentUser,
    service: ProgressServiceDep,
) -> CourseProgress:
    """Mark a lesson complete or undo it, and return the recalculated totals."""
    return await service.set_lesson(claims.user_id, lesson_id, completed=payload.completed)


@router.delete("/progress", response_model=CourseProgress)
async def reset_progress(claims: CurrentUser, service: ProgressServiceDep) -> CourseProgress:
    """Start the programme over. Returns the (now empty) progress."""
    return await service.reset(claims.user_id)


@router.get("/{slug}", response_model=CourseModuleDetail)
async def get_course(slug: str, service: CourseServiceDep) -> CourseModuleDetail:
    return await service.get_module(slug)


@router.put("/{slug}", response_model=CourseModuleDetail, dependencies=[RequireAdmin])
async def update_course(
    slug: str, payload: CourseModuleUpdate, service: CourseServiceDep
) -> CourseModuleDetail:
    return await service.update_module(slug, payload)


@router.delete("/{slug}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[RequireAdmin])
async def delete_course(slug: str, service: CourseServiceDep) -> None:
    await service.delete_module(slug)
