#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 21_pyquery_nodes_operation.py
@time: 2018/9/7 21:54
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
li.remove_class('active')
print(li)
li.add_class('active')
print(li)

print("========= attr ==========")
html = '''
<ul class ="list">
<li class ="item-0 active"><a href="link3.html"><span class ="bold">third item</span></a></li>
</ul>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
# 修改一个属性
li.attr('name', 'link')
print(li)
# 改变纯文本
li.text('change item')
print(li)
# li内部html改变
li.html('<span>changed item</span>')
print(li)

html = """
<div class ="wrap">
H e l l 口 ， W o r l d
<p> This is a paragraph.</p>
</div>
"""
doc = pq(html)
warp = doc('.wrap')
print(warp.text())
# 移除 wrap节点下的p节点
warp.find('p').remove()
print(warp.text())
