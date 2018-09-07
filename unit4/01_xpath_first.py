#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 01_xpath_first.py
@time: 2018/9/7 13:29
"""
from lxml import etree

'''
xpath使用规则：
nodename    选取此节点的所有子节点
    /       从当前节点选取直接子节点
//          从当前节点选取子孙节点
.           选取当前节点
..          选取当前节点父节点
@           选取属性
'''

# etree解析HTML构建xpath    会将最后一个未闭合的li标签补全    并将HTML和body标签补全
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

#   该方式会多DOCTYPE声明，其它内容与上面保持一致
html = etree.parse('./test.html', etree.HTMLParser())

result1 = html.xpath('//*')
print(result1)
result2 = html.xpath('//li')
print(result2)
print(result2[0])

result = etree.tostring(html)
print(result.decode('utf-8'))

