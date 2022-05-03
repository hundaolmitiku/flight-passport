"""
Django settings for flight_passport project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
from dotenv import load_dotenv, find_dotenv
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
import json
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'oauth2_provider_jwt',
    'corsheaders',
    'authprofiles',
    'rolepermissions',
    'jws_operations',
    'allauth',
    'vault',
    'allauth.account',
    'allauth.socialaccount',
]
SITE_ID = 1


MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'flight_passport.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            os.path.join(BASE_DIR,'allauth', 'templates','allauth'),
            os.path.join(BASE_DIR,'vault', 'templates'),
            
            ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'vault.context_processors.from_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'flight_passport.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SOCIALACCOUNT_AUTO_SIGNUP = False 
ACCOUNT_AUTHENTICATION_METHOD  = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_ADAPTER = 'authprofiles.adapter.PassportAccountAdapter'
DEFAULT_FROM_EMAIL = 'Openskies Flight Passport Support <noreply@openskies.sh>'
LOGO_URL = 'https://about.openskies.sh/images/logo.svg'
APPLICATION_NAME = 'Openskies.sh - Trust Bridge'

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ACCOUNT_FORMS = {'signup': 'authprofiles.forms.PassportSignUpForm', 'login':'authprofiles.forms.PassportLoginForm',  'reset_password': 'authprofiles.forms.ResetPasswordForm',}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'flight_passport.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    'oauth2_provider.backends.OAuth2Backend',
)

JWT_ISSUER = 'Openskies'
JWT_ISSUER_DOMAIN = 'https://id.openskies.sh/'
JWT_ID_ATTRIBUTE = 'email'
JWT_PRIVATE_KEY_OPENSKIES = os.environ.get("OIDC_RSA_PRIVATE_KEY")

JWT_PAYLOAD_ENRICHER = 'vault.jwt_utils.payload_enricher'

SHOW_ADMIN = int(os.environ.get('SHOW_ADMIN'))

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SCOPES_BACKEND_CLASS = 'authprofiles.scopes'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

OAUTH2_PROVIDER = {
    # 'OAUTH2_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',
    'OIDC_ENABLED' :True,    
    'PKCE_REQUIRED': os.environ.get("PKCE_ENABLED",False), 
    "OIDC_RSA_PRIVATE_KEY": os.environ.get("OIDC_RSA_PRIVATE_KEY"),
    'APPLICATION_MODEL': 'authprofiles.PassportApplication',
    'SCOPES_BACKEND_CLASS' :'authprofiles.scopes.PassportScopes',
    "OAUTH2_VALIDATOR_CLASS": "authprofiles.oauth_validators.PassportOAuth2Validator",
    'REQUEST_APPROVAL_PROMPT':"auto",
    "ACCESS_TOKEN_EXPIRE_SECONDS" : 3600,
    "REFRESH_TOKEN_EXPIRE_SECONDS" : 3600,
    "ID_TOKEN_EXPIRE_SECONDS":3600, 
    
}

django_heroku.settings(locals())