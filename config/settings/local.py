from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '90ge0_p0g=e3j#8k5g=&1*u0e83n2&bvw_xeeb13#abqbf++%h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

# Application definition
INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'librarydb',
'USER': 'libraryuser',
'PASSWORD': 'library',
'HOST': 'localhost',
'PORT': '',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'