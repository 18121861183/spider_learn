#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 23_request_session.py
@time: 2018/9/6 16:40
"""

import requests

# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)

session = requests.Session()
session.get('http://httpbin.org/cookies/set/number/123456789')
r = session.get('http://httpbin.org/cookies')
print(r.text)
