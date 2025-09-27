"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

if 'RENDER' in os.environ:
    try:
        from startup import run_migrations

        run_migrations()
    except Exception as e:
        print(f"Startup migration failed: {e}")

application = get_wsgi_application()

application = get_wsgi_application()
