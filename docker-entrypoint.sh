#!/usr/bin/env bash
# Wait for Postgres, apply migrations, seed sample content, then start the API.
set -euo pipefail

echo "Applying database migrations..."
alembic upgrade head

echo "Seeding sample blog content..."
python -m scripts.seed

echo "Starting API server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
