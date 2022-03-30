#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
#File: __call__test.py
#Time: 2022/2/27 7:06 下午
#Author: julius
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('i was called')


if __name__ == "__main__":
    p=Person('julius')
    print(p.name)
