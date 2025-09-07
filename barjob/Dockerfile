# Python bazinis
FROM python:3.11-slim

# Sisteminės priklausomybės (psycopg2 ir pan.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

# Statiniai failai
RUN python manage.py collectstatic --noinput || true

ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Pakeisk `myproject` į savo projekto pavadinimą (kur wsgi.py)
CMD gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT
