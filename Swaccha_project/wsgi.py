import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from Swaccha_project.settings import STATIC_ROOT

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Swaccha_project.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
