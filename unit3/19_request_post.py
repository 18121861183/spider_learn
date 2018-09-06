#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 19_request_post.py
@time: 2018/9/6 15:33
"""
import requests

data = {'name': 'zyc', 'age': 22}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
