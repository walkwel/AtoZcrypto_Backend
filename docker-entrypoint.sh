#!/usr/bin/env bash
# Wait for Postgres, apply migrations, seed starter content, then start the API.
#
# Failure policy is deliberate and differs per step:
#   * waiting and migrations are FATAL — serving requests against an
#     unreachable or out-of-date schema produces errors on every route, so
#     failing here is better than starting.
#   * seeding is NON-FATAL — it inserts editorial content and has no bearing on
#     whether the API can serve. A seed error used to abort this script before
#     `exec uvicorn`, taking the whole site down (nginx 502 on every route,
#     including /health) for what is only missing content. Log it loudly and
#     start anyway; the content can be seeded afterwards without an outage.
set -euo pipefail

echo "Waiting for the database..."
python -m scripts.wait_for_db 60

echo "Applying database migrations..."
alembic upgrade head

echo "Seeding starter content..."
seed_status=0
python -m scripts.seed || seed_status=$?
if [ "$seed_status" -eq 0 ]; then
  echo "Seeding complete."
else
  echo "WARNING: seeding failed (exit ${seed_status}). Starting the API anyway — content may be missing."
  echo "WARNING: re-run 'python -m scripts.seed' once the cause is fixed."
fi

echo "Starting API server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
