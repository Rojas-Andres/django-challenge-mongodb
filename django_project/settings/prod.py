import os

from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default=[])


DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": os.environ.get("MONGO_NAME"),  # Replace with your MongoDB database name
        "HOST": os.environ.get(
            "MONGO_HOST"
        ),  # Replace with your MongoDB host (e.g., MongoDB Atlas URI)
        "PORT": os.environ.get(
            "MONGO_PORT", 27017
        ),  # Replace with your MongoDB port (default is 27017)
        "USERNAME": os.environ.get(
            "MONGO_USER"
        ),  # Replace with your MongoDB username (if using authentication)
        "PASSWORD": os.environ.get(
            "MONGO_PASSWORD"
        ),  # Replace with your MongoDB password (if using authentication)
        "AUTH_SOURCE": os.environ.get(
            "MONGO_PASSWORD"
        ),  # Replace with the authentication database (default is 'admin')
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
