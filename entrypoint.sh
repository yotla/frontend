#!/bin/bash
set -e

# cores=$(nproc) && echo "nproc detected ${cores} available in container"

# echo "Starting uvicorn server with ${cores} workers"

exec uvicorn src.main:app --host "${HOST:-0.0.0.0}" --port "${PORT:-8000}" --workers 1