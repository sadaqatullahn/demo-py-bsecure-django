from os import environ
# import django_heroku
if environ.get('DEBUG', True):
    from .development import *
else:
    from .production import *


bSecure = {
    'client_id': '68d148bf-ff54-4740-8bc1-f70d08b39bff',
    'client_secret': 'OFv97Npd8s6xObGx/VCzHfrHklq7MwCGdA11Bbdaq14='
}

django_heroku.settings(locals())
