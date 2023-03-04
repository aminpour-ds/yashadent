from .common import *
import os
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['yashadent.com/', 'yashadent.ir/']   # just domain name without https://

DATABASES = {
    'default': dj_database_url.config()
}