#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 20_pyquery_value.py
@time: 2018/9/7 21:28
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
a = doc('.item-0.active a')
print(a, type(a))
# 获取属性值
print(a.attr('href'))
print(a.attr.href)

a = doc('a')
for item in a.items():
    print(item.attr('href'))

# 获取a表情内文本值
a = doc('a')
for item in a.items():
    print(item.text())

print('========= value =========')
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
li = doc('.item-0.active')
print(li)
# 第一个li标签内的纯文本
print(li.html())


print("=============== 2 =================")
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
li = doc('li')
# 返还第一个li标签内的纯文本
print(li)
# 所有li标签内的纯文本
print(li.text())
print(type(li.text()))
