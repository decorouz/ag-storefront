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

if DEBUG:
    MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]
