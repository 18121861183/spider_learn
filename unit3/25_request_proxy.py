#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 25_request_proxy.py
@time: 2018/9/6 16:55
"""
import requests

'''
基本代理方式
'''
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'https://10.10.1.10:1080'
}
r = requests.get('https://www.taobao.com', proxies=proxies)
print(r.text)

'''
http basic auth
'''
proxies = {
    'http': 'http://user:password@10.10.1.10:3128'
}
requests.get('https://www.taobao.com', proxies=proxies)

'''
socks代理
'''
proxies = {
    'http': 'sockss://user:password@host:port'
}
requests.get('https://www.taobao.com', proxies=proxies)
