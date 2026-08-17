from functools import lru_cache
from typing import Self

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

DEV_JWT_SECRET = "dev-insecure-secret-change-me"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    environment: str = "development"
    log_level: str = "INFO"

    database_url: str = "postgresql+asyncpg://crypto:crypto@localhost:5432/cryptolens"
    redis_url: str = "redis://localhost:6379/0"

    newsdata_api_key: str = ""
    newsdata_base_url: str = "https://newsdata.io/api/1"
    news_cache_ttl: int = 300
    news_refresh_interval: int = 900

    coingecko_base_url: str = "https://api.coingecko.com/api/v3"
    market_cache_ttl: int = 120

    # Blogs: platform-owned content plus articles aggregated from crypto RSS
    # feeds. Sources are defined in blog/providers/rss/feeds.py; this setting is
    # a comma-separated allow-list of their slugs (empty = every feed).
    blog_rss_feeds: str = ""
    blog_cache_ttl: int = 600
    blog_refresh_interval: int = 3600

    # --- Authentication (JWT) ---
    # Secret signing key. MUST be overridden in production; the app refuses to
    # start with the development default when ENVIRONMENT=production.
    jwt_secret_key: str = DEV_JWT_SECRET
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30
    password_reset_token_expire_minutes: int = 30

    # Optional bootstrap admin, created/updated by `python -m scripts.create_admin`.
    admin_email: str = ""
    admin_password: str = ""

    # Comma-separated list; kept as str because pydantic-settings JSON-decodes list fields.
    cors_origins: str = "http://localhost:3000"

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    @property
    def is_production(self) -> bool:
        return self.environment == "production"

    @model_validator(mode="after")
    def _reject_insecure_production_secret(self) -> Self:
        """Fail fast rather than sign production tokens with a public secret."""
        if self.is_production and self.jwt_secret_key == DEV_JWT_SECRET:
            raise ValueError("JWT_SECRET_KEY must be set to a strong secret in production.")
        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()
