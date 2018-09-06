#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 24_request_https.py
@time: 2018/9/6 16:45
"""
import requests
# 忽略警告
import urllib3
urllib3.disable_warnings()
# 通过日志捕获异常
# import logging
# logging.captureWarnings(True)

# 不验证ssl证书
response = requests.get('https://www.12306.cn', verify=False)
print(response.text)

# 证书读取方式
response = requests.get('https://www.12306.en', cert=('/path/server.crt', '/path/key'))
print(response .status_code)
