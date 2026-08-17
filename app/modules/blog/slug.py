"""Slug and reading-time helpers for blogs."""

import re

_SLUG_STRIP = re.compile(r"[^a-z0-9]+")
_WORDS_PER_MINUTE = 200


def slugify(text: str) -> str:
    """Turn a title into a URL-safe slug. Falls back to 'post' when empty."""
    slug = _SLUG_STRIP.sub("-", text.lower()).strip("-")
    return slug or "post"


def estimate_reading_time(content: str) -> int:
    """Estimate reading time in minutes from word count (min 1)."""
    words = len(content.split())
    return max(1, round(words / _WORDS_PER_MINUTE))
