"""
ASGI config for mysaas project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysaas.settings")

application = get_asgi_application()
fastapp = FastAPI(
    servers=[
        {
            "url": "/api/v1",
            "description": "V1",
        }
    ]
)


def init(app: FastAPI):
    @app.get("/health")
    def health_check():
        return {'status': 'ok'}


init(fastapp)
