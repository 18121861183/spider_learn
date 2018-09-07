#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 19_pyquery_iterator.py
@time: 2018/9/7 21:23
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
li = doc('.item-0.active')
print(li)
print(str(li).strip())
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))
