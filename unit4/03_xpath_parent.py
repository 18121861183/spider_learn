#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 03_xpath_parent.py
@time: 2018/9/7 14:12
"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
