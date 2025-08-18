from pathlib import Path
import os
import socket
import dj_database_url
from decouple import config
import dotenv
dotenv.load_dotenv()
from django.contrib.messages import constants as messages
from urllib.parse import urlparse, urlunparse

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.onrender.com', 'swacha.onrender.com', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myAuth',
    'profiles',
    'booking'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Swaccha_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Swaccha_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


BASE_DIR = Path(__file__).resolve().parent.parent

db_url = os.environ.get("DATABASE_URL", "")

def force_ipv4_in_db_url(url: str) -> str:
    if not url:
        return url
    p = urlparse(url)
    # Ensure a db name exists (Supabase default is 'postgres')
    path = p.path if p.path and p.path != "/" else "/postgres"
    # Resolve hostname to IPv4 (A record); avoids IPv6 AAAA selection
    ipv4 = socket.gethostbyname(p.hostname)
    # Rebuild URL with IPv4 literal in netloc
    netloc = f"{p.username}:{p.password}@{ipv4}:{p.port or 5432}"
    # Keep existing query; ensure sslmode=require present for libpq
    query = p.query
    if "sslmode=" not in (query or ""):
        query = (query + "&" if query else "") + "sslmode=require"
    return urlunparse((p.scheme, netloc, path, p.params, query, p.fragment))

DATABASES = {}

if db_url:
    db_url = force_ipv4_in_db_url(db_url)
    DATABASES["default"] = dj_database_url.parse(
        db_url,
        conn_max_age=600,
        ssl_require=True,  # Supabase needs SSL
    )
else:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
