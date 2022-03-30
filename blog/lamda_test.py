#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
#File: lamda_test.py
#Time: 2022/2/27 6:23 下午
#Author: julius
"""


def filter_method():
    return list(filter(lambda n:n % 2 == 1,range(1,20)))



if __name__ == "__main__":
    lists=[1,2,3,4,5,6]
    res = map(lambda x:x**2,lists)
    # print(type(res))
    res = list(res)
    print(type(res))
    for i in res:
        print(i)
    res = filter_method()
    print(res)