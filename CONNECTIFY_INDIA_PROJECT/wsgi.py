"""
WSGI config for CONNECTIFY_INDIA_PROJECT project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from os.path import join, dirname
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# print(os.environ['WEBSITE_HOSTNAME'])
settings_module='CONNECTIFY_INDIA_PROJECT.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'CONNECTIFY_INDIA_PROJECT.settings'

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CONNECTIFY_INDIA_PROJECT.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)


application = get_wsgi_application()
