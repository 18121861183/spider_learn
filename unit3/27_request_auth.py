#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 27_request_auth.py
@time: 2018/9/6 17:46
"""
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

# 登录认证
r = requests.get('https://192.168.5.130:5602', auth=HTTPBasicAuth('admin', 'colasoft'), verify=False)
print(r.text)

# 登录认证第二种方式
r = requests.get('https://192.168.5.130:5602', auth=('admin', 'colasoft'), verify=False)
print(r.text)

from requests_oauthlib import OAuthl
url = 'https : //a pi.twitter.com/1.1/account/verify credentials.json'
auth = OAuth1('YOUR _APP _KEY', 'YOUR_APP _SECRE T', 'USER_OAUTH_TOKEN ', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
