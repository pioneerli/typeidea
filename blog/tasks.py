#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
#File: tasks.py
#Time: 2022/3/30 2:26 下午
#Author: julius
"""
import time

from celery import Celery

from blog.celery import app


# 使用redis做为broker
# app = Celery('blog.tasks2',broker='redis://127.0.0.1:6379/0',backend='redis://127.0.0.1:6379/1')


# 创建任务函数
@app.task
def my_task(a, b, c):
    print('任务正在执行...')
    print('任务1函数休眠10s')
    time.sleep(10)
    return a + b + c


@app.task
def my_task2():
    print("任务2函数正在执行....")
    print('任务2函数休眠10s')
    time.sleep(10)

