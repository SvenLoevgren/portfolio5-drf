from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv
from datetime import timedelta
from decouple import config
import re

# Load environment variables from .env file
load_dotenv()

if os.path.isfile("env.py"):
    import env

JWT_SECRET_KEY = config("JWT_SECRET_KEY")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

TOKEN_KEY = os.environ.get('TOKEN_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

CSRF_TRUSTED_ORIGINS = [
    'https://github.com',
    'https://*.github.com',
    'https://herokuapp.com',
    'https://*.herokuapp.com',
    'https://*.gitpod.io'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.views.static',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'avatar',
    'corsheaders',
    'fastfood',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    # Longer access token lifetime
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),
    # Refresh token lifetime
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=14),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    # Grace period for token refresh
    'SLIDING_TOKEN_REFRESH_LIFETIME_GRACE_PERIOD': timedelta(days=6),
    'SLIDING_TOKEN_REFRESH_LIFETIME_ALLOW_SAME_ORIGIN': False,
    'SLIDING_TOKEN_REFRESH_LIFETIME_ALTERNATE_REFRESH_URLS': None,
}

# 30 minutes in seconds = 1800
SESSION_COOKIE_AGE = 1800

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(
        r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'django_project_fastfood.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, os.path.join(TEMPLATES_DIR, 'rest_framework')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project_fastfood.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    ]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_VERIFICATION = 'none'

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL")),
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test_db.sqlite3',
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# NOTE!! Whitenoise used for static files since no upload of media is implemented yet.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# NOTE!! Whitenoise used for static files since no upload of media is implemented yet.
MEDIA_URL = '/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
