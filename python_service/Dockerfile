FROM python:3.12-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./

COPY common ./common
COPY python_service ./python_service

RUN uv sync --frozen --package python_service

CMD ["uv","run","--package","python_service","python","-m","python_service.app.main"]