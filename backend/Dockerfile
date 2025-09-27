FROM python:3.13-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PATH="/root/.local/bin:$PATH"
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

FROM base AS deps
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

FROM base AS devdeps
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --dev

FROM devdeps AS src
COPY . .

FROM src AS lint
RUN uv run ruff format --check

FROM deps AS runtime
WORKDIR /app
COPY --from=src /app /app
EXPOSE 8000
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
