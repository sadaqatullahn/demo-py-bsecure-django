
from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['bsecure-python-app.herokuapp.com',  '*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ('DATABASE_URL'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}
#
# STRIPE_PUBLIC_KEY = config('BSECURE_LIVE_CLIENT_ID')
# STRIPE_SECRET_KEY = config('BSECURE_LIVE_CLIENT_SECRET')
bSecure = {
    'client_id': '68d148bf-ff54-4740-8bc1-f70d08b39bff',
    'client_secret': 'OFv97Npd8s6xObGx/VCzHfrHklq7MwCGdA11Bbdaq14='
}
