#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 03_file_csv_write.py
@time: 2018/9/7 23:10
"""
import csv

# newline添加，防止多一个空行
with open('data.csv', 'w', newline='') as file:
    # 默认按照逗号分隔， delimiter设置按照指定符合分隔
    write = csv.writer(file, delimiter=',')
    write.writerow(['id', 'name', 'age'])
    write.writerow(['1000', 'mike', 22])
    write.writerow(['1001', 'tom', 21])
    write.writerow(['1002', 'lucy', 20])
    # 可同时写入多行
    write.writerows([['1003', 'rose', 24], ['1004', 'jack', 19]])

'''
字典方式写入csv
'''
with open('data2.csv', 'w', newline='') as file:
    fieldnames = ['id', 'name', 'age']
    write = csv.DictWriter(file, fieldnames=fieldnames)
    write.writeheader()
    write.writerow({'id': '1001', 'name': 'tom', 'age': 23})
    write.writerow({'id': '1002', 'name': 'jack', 'age': 22})
    write.writerow({'id': '1003', 'name': 'lucy', 'age': 21})

# 指定编码。解决中文乱码问题
with open('data2.csv', 'a', newline='', encoding='utf-8') as file:
    fieldnames = ['id', 'name', 'age']
    write = csv.DictWriter(file, fieldnames=fieldnames)
    write.writerow({'id': '1004', 'name': 'rose', 'age': 20})
