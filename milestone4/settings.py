"""
Django settings for milestone4 project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url
#import env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# To be Changed
#Old Secret Key this is now retired
#SECRET_KEY = 'f6kr-^t-^n)&j81^w-=o!m2r+x@1rv13xcynrh@i@e+0jabz7*'
SECRET_KEY = os.environ.get("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
# To be Changed
DEBUG = False

ALLOWED_HOSTS = [
    'milestone4jb.herokuapp.com',
    '127.0.0.1'
]


# Application definition

#storages added for s3 bucket
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'threelite',
    'threeauth',
    'posts',
    'storages',
    'django_forms_bootstrap',
    'threeshop',
    'threecart',
    'threecheckout',
    'threecontact'
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

ROOT_URLCONF = 'milestone4.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'threecart.contexts.cart_contents'
            ],
        },
    },
]

WSGI_APPLICATION = 'milestone4.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#if "DATABASE_URL" in os.environ:
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
#else:
 #   print("Postgres URL not found, using sqlite instead")
  #  DATABASES = {
   #     'default': {
    #        'ENGINE': 'django.db.backends.sqlite3',
     #       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      #  }
    #}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#amazon s3 storage 
AWS_S3_OBJECT_PARAMETERS = {
    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl':'max-age=94608000'
}

AWS_STORAGE_BUCKET_NAME = 'threeshop'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

#linked to customer_storages.py
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = 'https//%s/%s/'% (AWS_S3_CUSTOM_DOMAIN,STATICFILES_LOCATION)

#removed below for heroku
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#media settings
MEDIA_URL = 'https//%s/%s/'% (AWS_S3_CUSTOM_DOMAIN,MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIA_ROOT = 'https//%s/%s/'% (AWS_S3_CUSTOM_DOMAIN,MEDIAFILES_LOCATION)
MEDIAFILES_STORAGE = 'custom_storages.MediaStorage'

#stripe keys
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
