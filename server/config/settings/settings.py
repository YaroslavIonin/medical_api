import os
from pathlib import Path


BASE_DIR = Path(__file__).parents[2]
SECRET_KEY = 'django-insecure-v%r52)ezzsrfgwetrw13#aocuwgg+1)#wertrtg(md2lyob^m^)d5f*4=iq-0iktg1'
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']
SITE_ID = 1

##################################################################
# Debug settings (with docker)
##################################################################

DEBUG = True
print(DEBUG)
##################################################################
# Databases settings (with docker)
##################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'medicaldb',
    }
}

###################################################################
# Templates, middleware settings
##################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
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
]

##################################################################
# Static files settings (CSS, JavaScript, Images)
##################################################################

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATICFILES_DIRS = ('static',)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

##################################################################
# Default auto field settings
##################################################################

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

##################################################################
# SWAGGER
##################################################################

SWAGGER_SETTINGS = {
   'DEFAULT_INFO': 'config.swagger.api_info',
}
