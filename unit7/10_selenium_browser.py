#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 10_selenium_browser.py
@time: 2018/9/12 16:42
"""
import time

from selenium import webdriver

# 前进后退
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
browser.get('https://www.baidu.com')
browser.get('https://www.python.org')
browser.back()
time.sleep(1)
browser.forward()
time.sleep(5)
browser.close()
