#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 13_beautiful_soup_text.py
@time: 2018/9/7 17:07
@:keyword 匹配节点文本
"""
import re
from bs4 import BeautifulSoup

html = '''
<div class="panel">
<div class="panel-body">
<a> Hello, this is a link</a>
<a> Hello, this is a link, too </a>
</div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))
