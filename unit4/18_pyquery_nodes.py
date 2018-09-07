#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 18_pyquery_nodes.py
@time: 2018/9/7 21:07
"""
from pyquery import PyQuery as pq
html = '''
<div class="wrap">
<div class="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
 </div>
'''
doc = pq(html)
items = doc('.list')
# 直接父节点获取
container = items.parent()
print(type(container))
print(container)
# 获取所有祖先节点
parents = items.parents()
print(type(parents))
print(parents)
# 根据条件选择祖先节点
parent = items.parents('.wrap')
print(parent)


# 获取兄弟节点
li = doc('.list .item-0.active')
print('li', li)
print(li.siblings())
# 根据条件选择兄弟节点
print(li.siblings('.active'))
