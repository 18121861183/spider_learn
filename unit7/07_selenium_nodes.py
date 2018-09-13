#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 07_selenium_nodes.py
@time: 2018/9/12 15:20
"""
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
# 获取属性
print(logo.get_attribute('class'))

# 获取文本值
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

# 获取id 位置，标签名和大小
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
