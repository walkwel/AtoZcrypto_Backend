"""Shared response schemas used across modules."""

from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Pagination(BaseModel):
    page: int
    limit: int
    total: int
    has_next: bool


class Page(BaseModel, Generic[T]):
    """Standard list envelope: {"data": [...], "pagination": {...}}."""

    data: list[T]
    pagination: Pagination

    @classmethod
    def create(cls, items: list[T], page: int, limit: int, total: int) -> "Page[T]":
        return cls(
            data=items,
            pagination=Pagination(
                page=page,
                limit=limit,
                total=total,
                has_next=page * limit < total,
            ),
        )
