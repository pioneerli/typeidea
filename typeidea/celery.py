#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
#File: celery.py
#Time: 2022/3/30 12:25 下午
#Author: julius
"""
import os
from celery import Celery
from blog import celeryconfig
project_name='typeidea'
# set the default django setting module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','typeidea.settings')
app = Celery(project_name)

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()