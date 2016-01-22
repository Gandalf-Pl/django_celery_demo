# -*- coding: utf-8 -*-

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_demo.settings")


from django.conf import settings

app = Celery("demo")

app.config_from_object("django.conf:settings")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
