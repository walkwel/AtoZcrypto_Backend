from datetime import datetime

from pydantic import BaseModel, ConfigDict

# Canonical category list. `all` is a filter alias handled by the service,
# never stored on a row.
NEWS_CATEGORIES: tuple[str, ...] = (
    "bitcoin",
    "ethereum",
    "altcoins",
    "defi",
    "regulation",
    "markets",
    "web3",
)


class NewsArticleOut(BaseModel):
    """Public news shape — the only news contract the frontend depends on."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    external_id: str
    title: str
    description: str | None
    source: str | None
    article_url: str
    image_url: str | None
    category: str
    published_at: datetime


class NewsCategory(BaseModel):
    slug: str
    label: str
