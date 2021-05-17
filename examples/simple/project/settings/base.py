"""
Django settings for simple project.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

from .core import PROJECT_DIR, gettext

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    from .local_settings import DEBUG_TEMPLATE
except Exception as err:
    DEBUG_TEMPLATE = False

try:
    from .local_settings import USE_CACHED_TEMPLATE_LOADERS
except Exception as err:
    USE_CACHED_TEMPLATE_LOADERS = False

if USE_CACHED_TEMPLATE_LOADERS:

    _TEMPLATE_LOADERS = [
        (
            "django.template.loaders.cached.Loader",
            (
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ),
        ),
    ]
else:

    _TEMPLATE_LOADERS = [
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    ]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # 'APP_DIRS': True,
        "DIRS": [PROJECT_DIR(os.path.join("..", "templates"))],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": _TEMPLATE_LOADERS,
            "debug": DEBUG_TEMPLATE,
        },
    },
]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "uzc&9xi6b#dz^z7tpa+br3ohq)-9%v9ux@9^t!(5fl41n%&mn$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEV = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Example
    "product",
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = PROJECT_DIR(os.path.join(BASE_DIR, "static"))
# Do not put any settings below this line
try:
    from .local_settings import *
except Exception as err:
    pass

# Make the `django-nine` package available without installation.
if DEV:
    source_path = os.environ.get("VALUTA_SOURCE_PATH", "src")
    # sys.path.insert(0, os.path.abspath('src'))
    sys.path.insert(0, os.path.abspath(source_path))
