import os
from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env()

SECRET_KEY = "u8x/A?D(G+KbPeSgVkYp3s6v9y$B&E)H@McQfTjWmZq4t7w!z%C*F-JaNdRgUkXp2r5u8x/A?D(G+KbPeShV"

# Build paths inside the project like this: PROJECT_ROOT / 'subdir'.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
env.read_env(os.path.join(PROJECT_ROOT, ".env"))

# app route directory function
app_path = environ.Path(__file__) - 3

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "corsheaders",
    "debug_toolbar",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "rest_framework_simplejwt",
    "apps.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = ["127.0.0.1", ]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "wiz.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI_APPLICATION = "wiz.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "HOST": env("SQL_HOST"),
        "PORT": '',
        "NAME": env("SQL_DB"),
        "USER": env("SQL_USER"),
        "PASSWORD": env("SQL_PASSWORD"),
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
        },
    }
}

# Rest framework configuration
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "COERCE_DECIMAL_TO_STRING": False,
    "EXCEPTION_HANDLER": "apps.core.exceptions.app_exception_handler",
}

# Rest Jwt token
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": "Bearer",
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=env.int("JWT_EXPIRATION_DELTA_MINUTES", 30)
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
}

# Spectacular configuration
SPECTACULAR_SETTINGS = {
    "TITLE": "Python testing",
    "DESCRIPTION": "Python testing",
    "VERSION": "1.0.0",
    # Spectacular sidebar alautun configuration
    # "SWAGGER_UI_DIST": "SIDECAR",
    # "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    # "REDOC_DIST": "SIDECAR",
    "COMPONENT_SPLIT_REQUEST": True,
    "SCHEMA_PATH_PREFIX_TRIM": False,
    "APPEND_COMPONENTS": {
        "securitySchemes": {
            "bearerAuth": {  # arbitrary name for the security scheme
                "name": "Authorization",
                "in": "header",
                "type": "http",
                "scheme": "bearer",
                # "bearerFormat": "JWT",
            },
            "jwtAuth": {},
        }
    },
    "SORT_OPERATIONS": False,
    "SECURITY": [{"bearerAuth": []}]
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = "/media/"

# Static storage configuration
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# other configurations
APPEND_SLASH = False
