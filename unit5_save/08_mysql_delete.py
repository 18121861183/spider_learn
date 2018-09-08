#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 08_mysql_delete.py
@time: 2018/9/8 11:53
"""
import pymysql

db = pymysql. connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age>20'

sql = 'delete from {table} where {conditon}'.format(table=table, conditon=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
