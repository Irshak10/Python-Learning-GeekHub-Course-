"""
WSGI config for aa_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import whitenoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aa_main.settings')

application = get_wsgi_application()
application = whitenoise
