FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY src/ ./src/
COPY data/ ./data/

CMD ["uv", "run", "python", "-m", "src.main", "schedule"]
