"""
WSGI config for python10 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from api_fetchers.household_vehicle_fetcher import fetch_and_store_vehicle_data as fasvd
from django.core.wsgi import get_wsgi_application
from api_fetchers.household_income_fetcher import fetch_and_store_income_data as fasid
from api_fetchers.UACSS_fetcher import fetch_and_store_UACSS_data as fasuad

#fasuad()
#fasid()
#fasvd()  # Fetch and store data before starting the server
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python10.settings")

application = get_wsgi_application()
