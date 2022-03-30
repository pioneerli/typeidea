#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
#File: logging_test.py
#Time: 2022/2/28 11:09 下午
#Author: julius
"""
import logging
from logging.config import dictConfig

logging_config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
        }

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': logging.DEBUG,
            'propagate': True,
        },
        'simple': {
            'handlers': ['console', 'file'],
            'level': logging.ERROR,
            'propagate': True,
        }
    },
}
if __name__ == "__main__":
    dictConfig(logging_config)
    print(__name__)
    logger = logging.getLogger(__name__)
    logger.debug('this is debug message')
