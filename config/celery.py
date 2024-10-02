# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django settings modulini o'rnatish
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Django settings ni yuklash
app.config_from_object('django.conf:settings', namespace='CELERY')

# Asinxron vazifalar uchun qayta yuklash
app.autodiscover_tasks()
