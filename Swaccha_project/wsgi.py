"""
WSGI config for Swaccha_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from pathlib import Path
from django.core.wsgi import get_wsgi_application

from Swaccha_project.settings import BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Swaccha_project.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=BASE_DIR / 'staticfiles')
