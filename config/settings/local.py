from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['LOCAL_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

# Application definition
INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'librarydb',
'USER': 'libraryuser',
'PASSWORD': DATABASE_PASSWORD,
'HOST': 'localhost',
'PORT': '',
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'catalog/staticfiles')
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'catalog/static'),
   ]

# Redirect to home URL after login
LOGIN_REDIRECT_URL = '/'