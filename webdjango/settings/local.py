"""
Django settings for webdjangular project Staging environment.

"""


from .base import *

DEBUG = True

SECRET_KEY = "21321321321321321"


INSTALLED_APPS += [

]

DATABASES = {
    'default': {
        'ENFORCE_SCHEMA': False,
        'ENGINE': 'djongo',
        'NAME': 'webdjangularr',
    }
}
