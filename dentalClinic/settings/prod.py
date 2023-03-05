from .common import *
import os


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['yashadent.ir', 'www.yashadent.ir', 'yashadent.com', 'www.yashadent.com']   # just domain name without https://

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'), 
        'USER': os.environ.get('DB_USER'), 
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}