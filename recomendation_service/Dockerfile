FROM python:3.11.5-slim-bullseye AS builder

WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.7.1 \
    && poetry config virtualenvs.in-project true \
    && poetry install --without dev --no-interaction --no-ansi

FROM python:3.11.5-slim-bullseye

COPY --from=builder /app /app

CMD ["/app/.venv/bin/main", "app:app", "--host", "0.0.0.0", "--port", "80"]