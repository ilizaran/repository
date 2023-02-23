"""
Django settings for repository project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import socket
from environ import Env               

env = Env()                           
env.read_env()

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath('%s' % os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY') 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  env.bool('DEBUG')
ALLOWED_HOSTS = ['*']


STATIC_ROOT = os.path.join(BASE_DIR, 'static-root')
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
        os.path.join(PROJECT_PATH, 'static'),

    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MEDIA_URL = '/datos/'
MEDIA_ROOT = os.path.join(BASE_DIR,'servidor')
FILEBROWSER_DIRECTORY = ''
VERSIONS_BASEDIR = "versions"

FILEBROWSER_EXTENSIONS ={
    'Image': ['.jpg','.jpeg','.gif','.png'],
    'Document': ['.pdf','.odt','.rtf','.txt','.odc','.csv','.svg','tiff','.tif'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.mp4','.vob'],
    'Audio': ['.mp3','.wav','.flac','.midi',]
}


FILE_UPLOAD_MAX_MEMORY_SIZE = 214958080 # 250MB
FILEBROWSER_MAX_UPLOAD_SIZE = 214958080 # 250MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000
#DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600 # 10MB

# Application definition

INSTALLED_APPS = (
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tables2',
    'django_filters',
    'django.contrib.humanize',
    'record',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['repository/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'repository.urls'

WSGI_APPLICATION = 'repository.wsgi.application'

FOOTER = env('FOOTER')
TITLE = env('TITLE')
IMAGEN_LOGO = env('IMAGEN_LOGO')
DESCRIPTION = env('DESCRIPTION')
URL = env('URL')

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DATABASE'),
        'USER': env('MYSQL_USER'),
        'PASSWORD': env('MYSQL_PASSWORD'),
        'HOST': env('MYSQL_HOST'),
        'PORT': env('MYSQL_PORT'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
