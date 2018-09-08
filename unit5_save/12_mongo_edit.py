#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 12_mongo_edit.py
@time: 2018/9/8 17:28
"""
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.test
collection = db.students
condition = {'name': 'ttttt'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)

result = collection.update(condition, {'$set': student})
print(result)

# 条件修改，更新条件为{'$inc': {'age': 1}} 也就是年龄加1 ，第一个符合条件的数据--年龄加1
condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)


# 删除符合条件的所有数据
result = collection.remove({'name': 'tttt'})
print(result)
# 删除符合条件的第一条数据 （官方推荐使用 delete_one  delete_many）
result = collection.delete_one({'name': 'tttt'})
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)

# 其它操作
'''
find_one_and_delete()   find_one_and_replace()  find_one_and_update()
对索引进行操作
create_index()      create_indexes()        drop_index()
'''
