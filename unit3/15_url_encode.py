#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 15_url_encode.py
@time: 2018/9/6 14:30
"""
from urllib.parse import quote, unquote

# url 中文转码
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

# url中文解码
url2 = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url2))
