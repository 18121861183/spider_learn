#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 06_mysql_insert.py
@time: 2018/9/8 9:39
"""
import pymysql

id = '20120002'
user = 'bob'
age = 20
db = pymysql. connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = "insert into students(id, name, age) values (%s, %s, %s)"
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()

db = pymysql. connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
data = {
    'id': '201809001',
    'name': 'ttttt',
    'age': 11
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('success')
        db.commit();
except:
    print('failed')
    db.rollback()
db.close()
