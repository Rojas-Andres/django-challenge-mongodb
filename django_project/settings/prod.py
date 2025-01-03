import os

from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default=[])


DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": os.environ.get("MONGO_NAME"),
        "HOST": os.environ.get("MONGO_HOST"),
        "PORT": 27017,
        "USERNAME": os.environ.get("MONGO_USER"),
        "PASSWORD": os.environ.get("MONGO_PASSWORD"),
        "AUTH_SOURCE": "admin",
        "CLIENT": {
            "host": os.environ.get("MONGO_CLIENT_HOST"),
        },
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = os.environ.get(
    "SECURE_CONTENT_TYPE_NOSNIFF", default=True
)
