#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 17_request.py
@time: 2018/9/6 14:50
"""

import requests
import re

# response = requests.get('http://httpbin.org/get?name=tom&age=22')
# print(response.text)
#
# data = {
#     'name': 'tom',
#     'age': 22
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
# print(r.json())

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
title = re.findall(pattern, r.text)
print(title)

# 响应
r = requests.get('http://www.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r. headers), r. headers)
print(type(r. cookies), r. cookies)
print(type(r. url), r. url)
print(type(r.history), r.history)
