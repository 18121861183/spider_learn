#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 05_mysql_init.py
@time: 2018/9/8 8:44
"""
import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('database version: ' + str(data))
# 新建数据库
cursor.execute("create database spiders default character set utf8")
# 选择数据库
cursor.execute("use spiders")
# 创建新表
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL PRIMARY KEY, name' \
      ' VARCHAR(255) NOT NULL, age INT NOT NULL)'
cursor.execute(sql)
db.close()

