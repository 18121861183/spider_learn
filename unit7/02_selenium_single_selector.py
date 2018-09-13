#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 02_selenium_single_selector.py
@time: 2018/9/10 11:40
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


'''
全部方法
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
'''
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')   # css选择器，选取ID为q的元素
input_third = browser.find_element_by_xpath('//*[@id="q"]')     # 选取任意标签id=q的标签
print(input_first, input_second, input_third)

# 另外一种节点选择方式
# 只选取到第一个节点
input = browser.find_element(By.ID, 'q')
print(input)

browser.close()
