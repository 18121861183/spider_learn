#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 02_xpath_children.py
@time: 2018/9/7 13:59
"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)

result1 = html.xpath('//ul//a')
print(result1)

# 这种获取不到结果。结果为空
result2 = html.xpath('//ul/a')
print(result2)
