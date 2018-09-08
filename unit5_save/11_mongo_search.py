#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 11_mongo_search.py
@time: 2018/9/8 12:31
"""
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')

# 等价于 db = client['test']
db = client.test
collection = db.students
# find_one查询单个结果  find()
result = collection.find_one({'name': 'ttttt'})
print(type(result))
print(result)
# 返回一个生成器对象
result = collection.find({'name': 'ttttt'})
print(type(result))
for res in result:
    print(res)

# count
count = collection.find().count()
print(count)
count = collection.find({'age': 20}).count()
print(count)

# 排序
result = collection.find().sort('name', pymongo.ASCENDING)
print([res['name'] for res in result])

# 分页查询
result = collection.find().sort('name', pymongo.ASCENDING).skip(1)
print([res['name'] for res in result])
# 跳过一个记录，取两条数据
result = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(2)
print([res['name'] for res in result])
