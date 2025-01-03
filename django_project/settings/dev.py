"""
Development settings
"""

import socket  # only if you haven't already imported this

from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

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
            "serverSelectionTimeoutMS": 10000,
            "maxIdleTimeMS": 60000,
            "retryReads": True,
            "connectTimeoutMS": 10000,
            "retryWrites": True,
            "maxPoolSize": 50,
            "minPoolSize": 10,
        },
    }
}

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())

SWAGGER_SETTINGS = {
    "VALIDATOR_URLS": [
        "http://localhost:8000/__debug__/",  # Agregue la ruta a la barra de herramientas de depuración aquí
    ],
}

# MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
# INSTALLED_APPS += ["debug_toolbar"]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
