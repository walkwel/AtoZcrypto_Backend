"""NewsData.io implementation of NewsProvider.

Maps NewsData's crypto endpoint response into `RawArticle`. All parsing is
defensive: missing image/description/source/date are tolerated, and articles
without a usable id or link are skipped rather than raising.
"""

import logging
from datetime import UTC, datetime

from app.core.config import Settings
from app.integrations.http_client import request_json
from app.modules.news.providers.base import NewsProvider, RawArticle
from app.modules.news.schemas import NEWS_CATEGORIES

logger = logging.getLogger(__name__)

# Map our internal categories to NewsData.io free-text search queries.
_CATEGORY_QUERY: dict[str, str] = {
    "bitcoin": "bitcoin",
    "ethereum": "ethereum",
    "altcoins": "altcoin OR solana OR cardano OR xrp",
    "defi": "defi OR decentralized finance",
    "regulation": "crypto regulation OR SEC crypto",
    "markets": "crypto market",
    "web3": "web3 OR blockchain",
}


class NewsDataProvider(NewsProvider):
    def __init__(self, settings: Settings) -> None:
        self._api_key = settings.newsdata_api_key
        self._base_url = settings.newsdata_base_url

    async def fetch_latest(
        self, *, category: str | None = None, limit: int = 50
    ) -> list[RawArticle]:
        if not self._api_key:
            logger.warning("NEWSDATA_API_KEY not set — returning no articles")
            return []

        params: dict[str, str | int] = {
            "apikey": self._api_key,
            "language": "en",
            "category": "business,technology",
        }
        if category and category in _CATEGORY_QUERY:
            params["q"] = _CATEGORY_QUERY[category]
        else:
            params["q"] = "cryptocurrency OR bitcoin OR ethereum"

        payload = await request_json(f"{self._base_url}/news", params=params, provider="newsdata")

        results = payload.get("results") or []
        articles: list[RawArticle] = []
        for item in results[:limit]:
            article = self._parse(item, category)
            if article is not None:
                articles.append(article)
        return articles

    def _parse(self, item: dict, requested_category: str | None) -> RawArticle | None:
        external_id = item.get("article_id")
        article_url = item.get("link")
        title = item.get("title")
        if not external_id or not article_url or not title:
            return None

        return RawArticle(
            external_id=str(external_id),
            title=str(title),
            description=item.get("description"),
            source=item.get("source_id") or item.get("source_name"),
            article_url=str(article_url),
            image_url=item.get("image_url"),
            category=self._resolve_category(item, requested_category),
            published_at=self._parse_date(item.get("pubDate")),
        )

    @staticmethod
    def _resolve_category(item: dict, requested_category: str | None) -> str:
        if requested_category and requested_category in NEWS_CATEGORIES:
            return requested_category
        # Infer from title/description keywords, defaulting to "markets".
        text = f"{item.get('title', '')} {item.get('description', '')}".lower()
        for slug in ("bitcoin", "ethereum", "defi", "regulation", "web3"):
            if slug in text:
                return slug
        return "markets"

    @staticmethod
    def _parse_date(value: str | None) -> datetime:
        if not value:
            return datetime.now(UTC)
        try:
            # NewsData returns "YYYY-MM-DD HH:MM:SS" in UTC.
            return datetime.fromisoformat(value).replace(tzinfo=UTC)
        except ValueError:
            return datetime.now(UTC)
