#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 07_mysql_update.py
@time: 2018/9/8 11:46
"""
import pymysql

db = pymysql. connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

sql = 'update students set age=%s where name=%s'
try:
    cursor.execute(sql, ('25', 'bob'))
    db.commit()
except:
    db.rollback()
db.close()
