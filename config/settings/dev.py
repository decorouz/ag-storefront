from .common import *

DEBUG = True

SECRET_KEY = "django-insecure-_s@(ra(08u=-782u-l%p^o_jf3s-w#f4e#o4^-)tzzn=3#zfoy"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "storefront",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "1241-Biola",
    }
}

# CELERY STUFF
CELERY_BROKER_URL = "redis://localhost:6379/1"  # 1 is the name of our db

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
EMAIL_HOST = "localhost"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 2525

if DEBUG:
    MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]
