#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 08_beautiful_soup.py
@time: 2018/9/7 15:44
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 初始化时补全html和body标签
soup = BeautifulSoup(html, 'lxml')
# 按照标准格式输出html
print(soup.prettify())
# 获取title标签的内容
print(soup.title.string)
# 类型tag
print(type(soup.title))
# 标签完整内容
print(soup.title)
print(soup.head)
print(soup.p)
print('----------------------------')
# 获取节点名称
print(soup.title.name)
# 获取属性
print(soup.p.attrs)
# 获取name属性
print(soup.p.attrs['name'])
# 另一种属性获取方式
print(soup.p['class'])
print(soup.p['name'])
# 获取第一个p节点的文本
print(soup.p.string)
##############################################
