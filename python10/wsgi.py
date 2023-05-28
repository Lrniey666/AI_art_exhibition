"""
WSGI config for python10 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from api_fetchers.household_vehicle_fetcher import fetch_and_store_vehicle_data as fasvd
from django.core.wsgi import get_wsgi_application

fasvd()  # Fetch and store data before starting the server
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python10.settings")

application = get_wsgi_application()
