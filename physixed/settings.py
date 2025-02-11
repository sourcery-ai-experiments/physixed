"""
Django settings for physixed project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from dotenv import dotenv_values

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y$lr3$o6)q^k-4mlnm!va5#inp9i6*5og7rlt98ngrc76gh^m#"  # noqa: S105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(dotenv_values(dotenv_path=".env").get("DJANGO_DEBUG", True))

allowed_hosts_fallback = "localhost 127.0.0.1 [::1]"
ALLOWED_HOSTS = dotenv_values(dotenv_path=".env").get("ALLOWED_HOSTS", allowed_hosts_fallback).split(" ")


# Admin

ADMINS = ("Leroy Teegelbeckers", "multiduckk@gmail.com")
MANAGERS = ADMINS

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS: list[str] = [
    # Third party apps
    #######################
]

LOCAL_APPS: list[str] = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "physixed.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "physixed.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / STATIC_URL.strip("/")
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LOGGING

LOG_FILENAME = BASE_DIR / "logs" / "django_logfile.log"
if not LOG_FILENAME.parent.exists():
    LOG_FILENAME.parent.mkdir()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": ("%(levelname)s :: %(module)s:%(funcName)s:%(lineno)s :: %(asctime)s :: %(message)s"),
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            # "when": "W0",  # leaved the TimedRotatingFileHandler out for now. Not working.
            "filename": LOG_FILENAME,
            "formatter": "verbose",
        },
    },
    "loggers": {"DEFINED BELOW": None},
}

try:
    from .px_production_apps import baseline_apps, production_apps
except ImportError as e:
    msg = "CRITICAL: Can't import `px_production_apps.py`"
    raise AssertionError(msg) from e

try:
    if bool(DEBUG) is True:
        from .px_development_apps import development_apps
except ImportError:
    msg = """
    -------------------------- `px_development_apps.py` file was not found.
    * You really should create that file by copying the template.
    * Using the production app list for now, but this is probably not what you want. *
    --------------------------
    """
    print(msg)  # noqa: T201
    development_apps = production_apps.copy()

logger: dict[str, dict] = {}
default_log_style = {
    "handlers": [
        "file",
    ],
    "level": "DEBUG",
}


def update_applist_logging(
    app_directory: str,
    logfiles: Sequence[str],
    installed_apps: list,
    logger: dict,
) -> None:
    """Update the installed apps and the logger with the app_directory and logfiles."""
    if app_directory not in installed_apps:
        installed_apps.append(app_directory)

    # This handles all regular cases, and the special case for "basic.apps.BasicCommonConfig"
    directory_base = app_directory.split(".")[0]
    for subfile in logfiles:
        logger[f"{directory_base}.{subfile}"] = default_log_style


# Uncomment later: for handling email when errors occur
# 'django.request': {'handlers': ['file', 'mail_admins'],'level': 'DEBUG','propagate': True, },
for app_directory, appdict in baseline_apps.items():
    update_applist_logging(app_directory, appdict.get("log_files", []), INSTALLED_APPS, logger)

if bool(DEBUG) is True:
    # We are on development/debug mode
    for app_directory, appdict in development_apps.items():
        update_applist_logging(app_directory, appdict.get("log_files", []), INSTALLED_APPS, logger)
else:
    # We are on production!
    for app_directory, appdict in production_apps.items():
        update_applist_logging(app_directory, appdict.get("log_files", []), INSTALLED_APPS, logger)

# Finally, store the list of loggers.
LOGGING["loggers"] = logger
