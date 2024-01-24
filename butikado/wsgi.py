"""
WSGI config for butikado project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
from django.conf import settings

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'butikado.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.MEDIA_ROOT)
application.add_files(os.path.join(settings.BASE_DIR, 'media'), prefix='media/')
