from pathlib import Path
import os
import dj_database_url
from django.contrib.messages import constants as messages

# (Remove decouple/dotenv/socket unless you use them)
# from decouple import config
# import dotenv
# dotenv.load_dotenv()

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core ---
SECRET_KEY = os.getenv('SECRET_KEY')  # ensure set in Render Runtime env

# Case-insensitive read of DEBUG
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Allow your Render app + local dev
ALLOWED_HOSTS = ['.onrender.com', 'swacha.onrender.com', '127.0.0.1', 'localhost']

# Required when DEBUG=False (use https)
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    # add custom domain if you later use one, e.g. 'https://yourdomain.com'
]

# --- Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myAuth',
    'profiles',
    'booking',
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # keep directly after SecurityMiddleware
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

# --- Database ---
DATABASES = {}
DB_URL = os.environ.get("DATABASE_URL", "")

if DB_URL:
    # Ensure SSL for Supabase (pooler)
    if "sslmode=" not in DB_URL:
        DB_URL += ("&" if "?" in DB_URL else "?") + "sslmode=require"

    DATABASES["default"] = dj_database_url.parse(
        DB_URL,
        conn_max_age=600,
        ssl_require=True,
    )
else:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }

# --- Password validators ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- I18N / TZ ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # optional, matches your locale
USE_I18N = True
USE_TZ = True

# --- Static files ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Security for production ---
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # If you see redirect issues, you can comment the next line:
    SECURE_SSL_REDIRECT = True
