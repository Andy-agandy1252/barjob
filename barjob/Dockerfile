# Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# Sisteminės priklausomybės (pillow kompiliacijai ir pan.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg62-turbo-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Įdiegiame Python priklausomybes
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Programos kodas
COPY . .

# (Pasirinktinai) surenkam statinius, jei nori build metu
# RUN python manage.py collectstatic --noinput

CMD gunicorn barjob.wsgi:application --bind 0.0.0.0:${PORT}
