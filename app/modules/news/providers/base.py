"""News provider interface.

A provider fetches raw articles from an upstream source and normalises them
into `RawArticle` — our internal, provider-agnostic shape. The service layer
depends only on this interface, so swapping NewsData.io for CryptoPanic,
Messari, etc. later means adding one implementation, not touching business
logic.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class RawArticle:
    external_id: str
    title: str
    description: str | None
    source: str | None
    article_url: str
    image_url: str | None
    category: str
    published_at: datetime


class NewsProvider(ABC):
    """Contract every news source implementation must satisfy."""

    @abstractmethod
    async def fetch_latest(
        self, *, category: str | None = None, limit: int = 50
    ) -> list[RawArticle]:
        """Fetch the most recent articles, optionally scoped to one category."""
        raise NotImplementedError
