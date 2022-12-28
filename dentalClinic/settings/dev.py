from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h0%p+r5ipzdx#)hyke2u=)o87*%+g@15uyn-+&gdvf#p^bf0_z'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yashadent',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Rroot#12345',
        'PORT': '3306',
    }
}


