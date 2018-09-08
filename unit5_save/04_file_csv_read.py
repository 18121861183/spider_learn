#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 04_file_csv_read.py
@time: 2018/9/7 23:57
"""
import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# 使用pandas读取
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
