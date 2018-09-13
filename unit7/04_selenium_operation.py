#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 04_selenium_operation.py
@time: 2018/9/10 13:47
"""
import time

'''
    交互操作
    输入iPad点击操作
'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
time.sleep(10)
browser.close()
