# Need to be redefined and tested
from B2R import secret

ENVIRONMENT_NAME = 'PRODUCTION'
ENVIRONMENT_COLOR = 'red'
DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travisdb',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SECRET_KEY = secret.DJANGO_SECRET_KEY

#########################################################
# LinkedIn Info
#########################################################

LINKEDIN_APPLICATION_RETURN_CALLBACK = 'http://localhost:8000/main'
LINKEDIN_PROFILE_URL = secret.LINKEDIN_PROFILE_URL
LINKEDIN_APPLICATION_KEY = secret.LINKEDIN_APPLICATION_KEY
LINKEDIN_APPLICATION_SECRET = secret.LINKEDIN_APPLICATION_SECRET
