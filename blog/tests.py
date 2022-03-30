from django.test import TestCase

# Create your tests here.

import time
import logging
import functools
import sys


def time_cs(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        # print(f"{func.__name__} start time {start}")
        res = func(*args, **kwargs)
        # print(f"{func.__name__} cost {time.time() - start}")
        logger.debug(f"{func.__name__} cost {time.time() - start}")
        return res

    return wrapper


@time_cs
def test_method():
    for i in range(200):
        # print(f'{i}')
        logger.debug('{i}')


def cache_it(func):
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = repr(*args, **kwargs)
        try:
            result = cache[key]
        except KeyError:
            result = func(*args, **kwargs)
            cache[key] = result
        return result

    return inner


@cache_it
def query(sql):
    time.sleep(1)
    result = "excute sql %s" % sql
    return result


def test(arg1, arg2=1):
    print(f"{arg1} {arg2}")


if __name__ == "__main__":
    # test_method()
    # logging.basicConfig(level=logging.DEBUG)
    # logging.debug('test info')

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    # print(logger)
    logger.setLevel(level=logging.DEBUG)
    logger.debug('test debug log')
    # print(logger)
    logger.debug('debug')
    # logger.debug('this is info msg')
    res = query('select * from User1')
    print(res)

    str = "114.114.114.114"
    print(str.split('/')[0])

    print(sys.version_info[0])
