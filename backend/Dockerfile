FROM python:3.9.6-alpine3.14
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add build-base && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev make ffmpeg curl

RUN adduser -D accuser
USER accuser

WORKDIR /backend

COPY --chown=accuser:accuser requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --user

COPY --chown=accuser:accuser . .

WORKDIR /

RUN export PATH="${PATH}:/home/accuser/.local/bin"