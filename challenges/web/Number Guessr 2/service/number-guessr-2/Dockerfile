FROM python:3.11-slim-bookworm

COPY . /app

RUN python3 -m pip install quart

WORKDIR /app

EXPOSE 1337

ENV PYTHONDONTWRITEBYTECODE=1

CMD ["hypercorn", "app:app", "--bind", "0.0.0.0:1337"]