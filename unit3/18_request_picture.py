#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 18_request_picture.py
@time: 2018/9/6 15:29
"""

import requests

r = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
