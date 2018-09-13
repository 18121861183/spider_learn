#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 05_selenium_drop.py
@time: 2018/9/10 13:55
"""
import time

'''
    动作链
    
'''
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
time.sleep(15)
browser.close()
