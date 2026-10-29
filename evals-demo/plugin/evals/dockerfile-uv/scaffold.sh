#!/usr/bin/env bash
# Le projet de départ : un service FastAPI minuscule, géré par uv.
set -euo pipefail

mkdir -p quote_service
cat > pyproject.toml <<'TOML'
[project]
name = "quote-service"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = ["fastapi>=0.115", "uvicorn>=0.32"]

[dependency-groups]
dev = ["pytest>=8"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
TOML

# Lockfile abrégé : l'agent doit seulement voir qu'il existe.
printf 'version = 1\nrequires-python = ">=3.13"\n' > uv.lock

touch quote_service/__init__.py
cat > quote_service/main.py <<'PY'
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
PY
