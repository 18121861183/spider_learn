#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 20_request_upload.py
@time: 2018/9/6 15:45
"""
import requests

file = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=file)
print(r.text)
