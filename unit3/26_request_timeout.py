#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 26_request_timeout.py
@time: 2018/9/6 17:02
"""
import requests

'''
timeout默认None，代表永久等待
        单位：秒
'''
r = requests.get('https://www.taobao.com', timeout=1)
print(r.status_code)

# 连接超时，读取超时
r = requests.get('https://www.taobao.com', timeout=(5, 11, 30))
