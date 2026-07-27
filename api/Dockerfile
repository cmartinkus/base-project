FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy workspace files
COPY pyproject.toml uv.lock ./

COPY common ./common
COPY api ./api

# Install dependencies from lock file
RUN uv sync --frozen --package api

EXPOSE 8000

CMD ["uv","run","--package", "api","uvicorn","main:app","--host","0.0.0.0","--port","8000"]