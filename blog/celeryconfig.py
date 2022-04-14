#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
#File: celeryconfig.py
#Time: 2022/3/30 2:54 下午
#Author: julius
"""

# 设置结果存储
from typeidea import settings
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# 设置代理人broker
BROKER_URL = 'redis://127.0.0.1:6379/1'
# celery 的启动工作数量设置
CELERY_WORKER_CONCURRENCY = 20
# 任务预取功能，就是每个工作的进程／线程在获取任务的时候，会尽量多拿 n 个，以保证获取的通讯成本可以压缩。
CELERYD_PREFETCH_MULTIPLIER = 20
# 非常重要,有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True
# celery 的 worker 执行多少个任务后进行重启操作
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100
# 禁用所有速度限制，如果网络资源有限，不建议开足马力。
CELERY_DISABLE_RATE_LIMITS = True

CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = settings.TIME_ZONE
DJANGO_CELERY_BEAT_TZ_AWARE = False
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

