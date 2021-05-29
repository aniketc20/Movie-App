"""
Django settings for Movie project.

Generated by 'django-admin startproject' using Django 3.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
<<<<<<< HEAD
=======
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
>>>>>>> 762d8d3c86a60385dee630e7bbc3c49c1bc742ba


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5-po0+miq_v)-@pb2u5(9!&o22&r7@bod_a*&0ow_ygy1d^#hn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = []
=======
ALLOWED_HOSTS = ['aniketmovieapp.herokuapp.com', '127.0.0.1']
>>>>>>> 762d8d3c86a60385dee630e7bbc3c49c1bc742ba


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App',
    'embed_video'
]

MIDDLEWARE = [
<<<<<<< HEAD
=======
    'whitenoise.middleware.WhiteNoiseMiddleware',
>>>>>>> 762d8d3c86a60385dee630e7bbc3c49c1bc742ba
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Movie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Movie.wsgi.application'
AUTH_USER_MODEL = 'App.Account'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
=======
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd874dg5s0nou3v',
        'HOST': 'ec2-54-87-112-29.compute-1.amazonaws.com',
        'PORT': '5432   ',
        'USER': 'ifmnuoxsjayrkq',
        'PASSWORD': '8ac01c37d2814469f5bd034d14853fdda215a06acdd0f59858ea00e611eac0cd',
>>>>>>> 762d8d3c86a60385dee630e7bbc3c49c1bc742ba
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]
STATIC_URL = '/static/'
<<<<<<< HEAD
=======
#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
>>>>>>> 762d8d3c86a60385dee630e7bbc3c49c1bc742ba
