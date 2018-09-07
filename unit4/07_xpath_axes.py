#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 07_xpath_axes.py
@time: 2018/9/7 15:20
"""
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')  # 所有父节点
print(result)
result = html.xpath('//li[1]/ancestor::div')    # 父节点div
print(result)
result = html.xpath('//li[1]/attribute::*')     # 获取li标签的所有属性
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')     # 获取a标签href为link1.html的 a 标签
print(result)
result = html.xpath('//li[1]/descendant::span')     # 获取所有子孙节点包含span的节点
print(result)
result = html.xpath('//li[1]/following::*[2]')  # 获取当前节点之后的所有节点中的第二个
print(result)
result = html.xpath('//li[1]/following-sibling::*')     # 获取当前节点之后的所有同级节点
print(result)
