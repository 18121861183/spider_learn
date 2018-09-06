# coding:utf-8
from urllib.parse import parse_qs, parse_qsl

query = 'name=gremey&age=23'
# 字典的方式解析结果 {'name': ['gremey'], 'age': ['23']}
print(parse_qs(query))
# 转化为元组组成的列表 [('name', 'gremey'), ('age', '23')]
print(parse_qsl(query))
