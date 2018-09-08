#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 10_mongo_insert.py
@time: 2018/9/8 12:15
"""
import pymongo
from pymongo import MongoClient

# 初始化连接
# client = pymongo.MongoClient(host='127.0.0.1', port=27017)
# 简单连接方式
client = MongoClient('mongodb://127.0.0.1:27017')

# 等价于 db = client['test']
db = client.test
collections = db.students   # 或者 collections = db['students']

student1 = {
    'id': '201809001',
    'name': 'ttttt',
    'age': 21,
    'gender': 'male'
}
student2 = {
    'id': '201809002',
    'name': '啊啊啊啊啊',
    'age': 22,
    'gender': 'male'
}
# result = collections.insert(student2)  单条插入
result = collections.insert([student1, student2])   # 多条插入
print(result)


'''
官方推荐使用 insert_one  和 insert_many
例子： collections.insert_one(student)
       collections.insert_many([student1, student2])
'''
