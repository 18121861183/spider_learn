#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 09_beautiful_soup_choose.py
@time: 2018/9/7 16:05
"""
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
# p的直接子节点列表
print(soup.p.contents)
# 获取子节点
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
# 获取所有的子孙节点
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)
