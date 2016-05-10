from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_tutorial.settings')

from django.conf import settings  # noqa

app = Celery('CeleryApp')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    BROKER_URL = 'django://',
)

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))