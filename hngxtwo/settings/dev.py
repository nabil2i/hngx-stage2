import os
import dj_database_url
from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1n8!k4@&m$5bhzj*(9fu-#p(e!2ewzu^zfqnn+%hmen4m_n6kw'
# SECRET_KEY = os.environ['SECRET_KEY']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'railway',
#     'USER': 'postgres',
#     'PASSWORD': '3wZtIfS92YtCfVFstC54',
#     'HOST': 'containers-us-west-185.railway.app',
#     'PORT': '7064',
#   }
# }


# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': os.environ.get('DB_NAME'),
#     'HOST': os.environ.get('DB_HOST'),
#     'USER': os.environ.get('DB_USER'),
#     'PASSWORD': os.environ.get('DB_PASS'),
#     'PORT': os.environ.get('DB_PORT'),
#   }
# }
