#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 13_selenium_exception.py
@time: 2018/9/12 17:02
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()

try:
    browser.get('https://www.baidu.com')
except TimeoutError:
    print('Time out')

try:
    browser.find_elements_by_id('hello')
except NoSuchElementException:
    print('no element')
browser.close()
