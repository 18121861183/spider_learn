#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 02_file_json.py
@time: 2018/9/7 22:43
"""
import json

# json格式数据键值要使用双引号，否则将无法加载为json对象
str = """
[{
"name": "Bob",
"gender": "male",
"birthday": "1992-10-18"
},{
"name" : "Selina",
"gender ": "female",
"birthday ": "1995-10-18"
}]
"""
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
# 推进使用方式，如果键名不存在不会报错
print(data[0].get('name'))
# 第二个参数代表默认值
print(data[0].get('age', 25))

# 写入文件
data = '''
[{
"name": "王伟",
"gender": "男",
"birthday": "1992-10-18"
},{
"name" : "Selina",
"gender ": "female",
"birthday ": "1995-10-18"
}]
'''
# indent代表json格式缩进
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))


# 读取json文件
with open('data.json', 'r', encoding='utf-8') as file:
    str = file.read()
    data = json.loads(str)
    print(data)



