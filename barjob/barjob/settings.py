# settings.py
import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url  # <-- pridėta

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY", "dev-fallback-key")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Railway domenui užteks taip, bet geriau skaityti iš env
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", ".railway.app,localhost,127.0.0.1").split(",")

INSTALLED_APPS = [
    'recipes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- pridėta
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'barjob.urls'
WSGI_APPLICATION = 'barjob.wsgi.application'

# --- Database (Railway Postgres, jei nustatytas DATABASE_URL); kitaip liks sqlite ---
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=bool(os.getenv("DATABASE_URL")),
    )
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Static/Media ---
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Naudoja optimizuotą statinių servinimą
STORAGES = {
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"}
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
