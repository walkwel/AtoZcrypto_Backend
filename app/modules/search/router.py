"""Search HTTP endpoint."""

from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.market.dependencies import get_market_service
from app.modules.market.service import MarketService
from app.modules.search.schemas import SearchResults
from app.modules.search.service import SearchService

router = APIRouter(prefix="/search", tags=["search"])


def get_search_service(
    db: Annotated[AsyncSession, Depends(get_db)],
    market_service: Annotated[MarketService, Depends(get_market_service)],
) -> SearchService:
    return SearchService(db, market_service)


@router.get("", response_model=SearchResults)
async def search(
    service: Annotated[SearchService, Depends(get_search_service)],
    q: Annotated[str, Query(min_length=2, max_length=100)],
) -> SearchResults:
    return await service.search(q)
