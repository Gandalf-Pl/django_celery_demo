# -*- coding: utf-8 -*-

from celery import shared_task


@shared_task(name="django_celery_demo.demo_app.tasks.add")
def add(x, y):
    return x + y
