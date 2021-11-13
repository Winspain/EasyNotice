# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 14:42
# @Author  : dicardo
# @File    : celery_app.py
# @Software: PyCharm

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easy_notice.settings.local")

app = Celery("easy_notice")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
