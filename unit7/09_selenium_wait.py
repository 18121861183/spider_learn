#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 09_selenium_wait.py
@time: 2018/9/12 15:49
"""
from selenium import webdriver

# 隐式等待，没找到节点时将等一段时间再查找DOM
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)

# 显示等待 排除网络条件的影响
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)

