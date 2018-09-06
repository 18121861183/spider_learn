#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 33_regex_compile.py
@time: 2018/9/6 23:06
"""
import re

# 正则对象反复使用
contentl = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 12:31'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', contentl)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
