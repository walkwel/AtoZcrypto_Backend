"""FastAPI application entry point.

Wires configuration, logging, shared clients, middleware, routers, and the
background news refresh into one deployable modular-monolith app.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging
from app.core.middleware import RequestContextMiddleware
from app.core.redis import init_cache
from app.core.scheduler import PeriodicScheduler
from app.integrations.http_client import close_http_client, init_http_client
from app.modules.blog.jobs import refresh_blogs_job
from app.modules.news.jobs import refresh_news_job

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    setup_logging(settings.log_level)
    init_cache()
    init_http_client()

    scheduler = PeriodicScheduler()
    scheduler.schedule(
        refresh_news_job,
        interval_seconds=settings.news_refresh_interval,
        name="news-refresh",
    )
    scheduler.schedule(
        refresh_blogs_job,
        interval_seconds=settings.blog_refresh_interval,
        name="blog-refresh",
    )
    logger.info("application started", extra={"environment": settings.environment})

    yield

    await scheduler.shutdown()
    await close_http_client()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title="AtoZ Crypto API",
        version="1.0.0",
        description="Crypto Market Intelligence platform API.",
        docs_url="/docs",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=True,
        # The API serves writes (auth, blog authoring), so preflight must permit
        # them — a GET-only policy silently breaks every browser mutation.
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type"],
    )
    app.add_middleware(RequestContextMiddleware)

    register_exception_handlers(app)
    app.include_router(api_router)
    return app


app = create_app()
