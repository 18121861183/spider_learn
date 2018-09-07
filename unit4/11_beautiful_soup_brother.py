#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 11_beautiful_soup_brother.py
@time: 2018/9/7 16:30
"""
from bs4 import BeautifulSoup
html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
soup = BeautifulSoup(html, 'lxml')
print('next', soup.a.next_sibling)
print('pre', soup.a.previous_sibling)
print('next lists', list(enumerate(soup.a.next_siblings)))
print('pre lists', list(enumerate(soup.a.previous_siblings)))
print('******************************************************************')

# 提取信息
html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        </p>
"""
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])
