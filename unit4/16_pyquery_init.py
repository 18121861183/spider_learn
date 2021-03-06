#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 16_pyquery_init.py
@time: 2018/9/7 17:30
"""
from pyquery import PyQuery as pq
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
# 获取li标签
print(doc('li'))

# 从网页直接获取数据进行解析
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

doc = pq(filename='test.html')
print(doc('li'))
