import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


celery = Celery("storefront")

celery.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
celery.autodiscover_tasks() 