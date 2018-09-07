#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 17_pyquery_css.py
@time: 2018/9/7 20:45
"""
from pyquery import PyQuery as pq
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
print(doc('#container .list li'))

doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
# 将符合条件的所有子孙节点选择出来
lis = items.find('li')
print(type(lis))
print(lis)
# 查询子节点
lis = items.children()
print(lis)
# 查询带active的子节点
lis = items.children('.active')
print(lis)


