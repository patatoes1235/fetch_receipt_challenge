FROM python:3.11-slim AS base

WORKDIR /usr/src/app

ENV PYTHONPATH "${PYTHONPATH}:$PWD"
ENV PTYHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt ./
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY . .

FROM base AS webserver
EXPOSE 8000
ENTRYPOINT uvicorn src.main:app --proxy-headers --host 0.0.0.0 --port 8000 $UVICORN_FLAGS