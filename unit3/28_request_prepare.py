#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 27_request_auth.py
@time: 2018/9/6 17:46
"""
from requests import Session, Request

url = 'http://httpbin.org/post'
data = {
    'name': 'zyc'
}
headers = {
    'User-Agent': 'Mozilla/s.o (Maci ntosh; Intel Mac OS X 10 _11_4) AppleWebKit/537.36 (KH TML, lik e Gecko )Chrome/53 .0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
