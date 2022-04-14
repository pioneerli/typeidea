#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
#File: celery.py
#Time: 2022/3/30 2:55 下午
#Author: julius
"""
import os

from celery import Celery

from blog import celeryconfig

# 为celery 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE","typeidea.settings")
# 创建celery app
app = Celery('blog')
# 从单独的配置模块中加载配置
app.config_from_object(celeryconfig)

# 设置app自动加载任务
app.autodiscover_tasks([
    'blog',
])

# 解决时区问题,定时任务启动就循环输出
# app.now = timezone.now
