#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: xx@xx.com
@software: PyCharm
@file: toutiao_spider.py
@time: 2018/9/8 18:07
"""
import requests
from urllib.parse import urlencode


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': '1'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

