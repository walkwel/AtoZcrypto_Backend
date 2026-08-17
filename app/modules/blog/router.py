"""Blog HTTP endpoints.

Reads are public. Writes (create/update/delete of internal blogs) require a
signed-in user with the admin role - see app/modules/auth/dependencies.py.
"""

from typing import Annotated

from fastapi import APIRouter, Query, status

from app.core.schemas import Page
from app.modules.auth.dependencies import RequireAdmin
from app.modules.blog.dependencies import BlogServiceDep
from app.modules.blog.schemas import (
    BlogCategory,
    BlogCreate,
    BlogDetail,
    BlogSummary,
    BlogUpdate,
)
from app.modules.blog.service import BlogWithRelated

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("", response_model=Page[BlogSummary])
async def list_blogs(
    service: BlogServiceDep,
    category: Annotated[str | None, Query()] = None,
    source: Annotated[str | None, Query()] = None,
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=50)] = 12,
) -> Page[BlogSummary]:
    return await service.list_blogs(category=category, source=source, page=page, limit=limit)


@router.post(
    "",
    response_model=BlogDetail,
    status_code=status.HTTP_201_CREATED,
    dependencies=[RequireAdmin],
)
async def create_blog(payload: BlogCreate, service: BlogServiceDep) -> BlogDetail:
    return await service.create_blog(payload)


# Declared before /{slug} so the literal path is matched first — otherwise the
# slug route would capture "categories".
@router.get("/categories", response_model=list[BlogCategory])
async def blog_categories(service: BlogServiceDep) -> list[BlogCategory]:
    return await service.list_categories()


@router.get("/{slug}", response_model=BlogWithRelated)
async def get_blog(slug: str, service: BlogServiceDep) -> BlogWithRelated:
    return await service.get_blog(slug)


@router.put("/{slug}", response_model=BlogDetail, dependencies=[RequireAdmin])
async def update_blog(slug: str, payload: BlogUpdate, service: BlogServiceDep) -> BlogDetail:
    return await service.update_blog(slug, payload)


@router.delete("/{slug}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[RequireAdmin])
async def delete_blog(slug: str, service: BlogServiceDep) -> None:
    await service.delete_blog(slug)

