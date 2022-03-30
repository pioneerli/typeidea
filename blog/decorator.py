#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
#File: decorator.py
#Time: 2022/2/28 8:50 上午
#Author: julius
"""
import time
import functools
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 使用闭包,引用外部变量
def log(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is called")
        return func(*args, **kwargs)

    return wrapper


def enhance_log(text):
    def decorate(func):
        # @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} is called")
            print(f"text is {text}")
            return func(*args, **kwargs)

        return wrapper

    return decorate


@enhance_log('enhance_log')
def now():
    print(time.time())


def func_cost_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(start_time)
        func(*args, **kwargs)
        logger.info(f"{func.__name__} excute in {time.time() - start_time} ms")
    return wrapper


@func_cost_time
def fast(x, y):
    time.sleep(5)
    print('sleep 5s')
    return x + y



@func_cost_time
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


# log(now) wrapper
# log(now)() wrapper() func.__name__ = log(now) time
if __name__ == "__main__":
    # res = now()
    # func_name = enhance_log('execute')(now)
    # print(func_name.__name__)

    # fast=func_cost_time(fast)(5,10)
    res = fast(5,10)
    time.sleep(2)
    print(f"res:{res}")
    # 闭包执行方式 func_cost_time(fast)(5,10)
    # 1、开始执行func_cost_time(fast) 方法 打印开始时间
    # 2、执行函数内逻辑
    # 3、开始执行wrapper 函数内的其他逻辑
    # slow_res = slow(5,10,15)