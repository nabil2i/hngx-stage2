from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j60!4&tm)#2p8d$)^%bfk3s6kuc1ou7#h-07#y1x8z_$tto2iw'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': ''
    }
}
