from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1n8!k4@&m$5bhzj*(9fu-#p(e!2ewzu^zfqnn+%hmen4m_n6kw'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'hngx2',
    'HOST': 'localhost',
    'USER': 'root',
    'PASSWORD': 'password'
  }
}