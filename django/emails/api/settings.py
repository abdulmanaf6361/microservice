import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '************YOUR SECRET KEY HERE************'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	'django.contrib.staticfiles',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'rest_framework',
	'rest_framework_swagger',

	'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emails',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres.cdwuwa0os4sh.ap-south-1.rds.amazonaws.com',  # Assuming PostgreSQL is running locally
        'PORT': '5432',        # Default PostgreSQL port
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = ''

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "abdulmanaf6361@gmail.com"
EMAIL_HOST_PASSWORD = "myrs mqtr lczp kpps"
EMAIL_USE_TLS = True