#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 09_mysql_query.py
@time: 2018/9/8 12:00
"""
import pymysql

db = pymysql. connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

sql = 'select * from students where age>=20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One: ', one)
    results = cursor.fetchall()
    print('results: ', results)
    print('results type: ', type(results))
    for row in results:
        print(row)
except:
    print('error')

# 按条遍历
try:
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print('Row: ', row)
        row = cursor.fetchone()
except:
    print('error')
