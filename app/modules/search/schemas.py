from pydantic import BaseModel

from app.modules.blog.schemas import BlogSummary
from app.modules.market.schemas import Coin
from app.modules.news.schemas import NewsArticleOut


class SearchResults(BaseModel):
    query: str
    news: list[NewsArticleOut]
    blogs: list[BlogSummary]
    coins: list[Coin]
