from .base import *


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER' : 'root',
        'PASSWORD' : 'e267e822',
        'HOST' : 'localhost',
        'PORT' : '3306'
    }
}
