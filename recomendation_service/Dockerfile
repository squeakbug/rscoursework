# syntax=docker/dockerfile:1.3
FROM python:3.11.5-slim-bullseye AS builder

WORKDIR /app
COPY recomendation_service ./recomendation_service
COPY data ./data

WORKDIR /app/recomendation_service
RUN python -m pip install --no-cache-dir poetry==1.7.1 \
    && poetry config virtualenvs.in-project true \
    && poetry install --without dev --no-interaction --no-ansi

CMD ["poetry", "run", "python", "src/telegram_interface/main.py"]
