# -*- encoding: utf-8 -*-

"""
Django settings for fusionsh project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lu1z%i60s377d5!a@(@z+jwhi!3gz0b%^ov*&@#mn8e3%ns8y@'

#fix django_compressor
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '104.131.54.188', '.fusionsh.com.ar', '.fusionsh.com.ar.', 'dev.fusionsh.com.ar', 'dev.fusionsh.com.ar.']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_countries',
    'django_markdown',
    'compressor',
    'bootstrap3',
    'runs',
    'news',
    'import_export',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fusionsh.urls'

WSGI_APPLICATION = 'fusionsh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fusionsh',
        'USER': 'cailo',
        'PASSWORD': 'lajdoque',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#    '/usr/share/nginx/www/fusion/fusionsh/static/',
#)

#STATIC_URL = 'http://static.fusionsh.com.ar/'
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#MEDIA_URL = 'http://media.fusionsh.com.ar/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Template dirs
# https://docs.djangoproject.com/en/1.7/ref/settings/#template-dirs

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

#Configuraciones para enviar mensajes usando gmail

EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'no-reply@fusionsh.com.ar'
EMAIL_HOST_PASSWORD = 'sl987654'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

