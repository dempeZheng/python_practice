#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '192.168.147.129',
        'port': 3306,
        'user': 'root',
        'password': 'mysql',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}