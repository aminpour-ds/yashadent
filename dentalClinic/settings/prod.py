from .common import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['192.168.1.20', 'localhost', '127.0.0.1']