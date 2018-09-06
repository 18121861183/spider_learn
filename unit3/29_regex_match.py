#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 29_regex_match.py
@time: 2018/9/6 21:20
"""
import re

'''
re.S 使.匹配包括换行在内的所有字符
re.I 使匹配大小写不敏感
------------------------ 非常用选项 ---------------------------
re.M 多行匹配，影响^和$
re.U 根据Unicode字符集解析字符，影响\w \W \b \B
----------------------------- 不理解？ ----------------------------------
re.L 使本地化识别（local-aware）匹配
re.X 使正则写的更容易理解  ？
'''

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d+\s\d{4}\s\w{10}', content)
print(result)
# 返回匹配中的结果
print(result.group())
# 返回 2 元组（m.start(group)， m.end(group))
print(result.span())


content2 = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^Hello\s(\d+)\sWorld', content2)
print(result2)
# 完整结果
print(result2.group())
# 第一个被（）包括的结果
print(result2.group(1))
print(result2.span())

result3 = re.match('^He.*?(\d+).*Demo$', content2)
print(result3)
print(result3.group(1))

# match匹配从头开始匹配，开头匹配不到则匹配失败
content3 = 'http://weibo.com/comment/kEraCN'
result4 = re.match('http.*?comment/(.*?)', content3)
result5 = re.match('http.*?comment/(.*)', content3)
print('result4', result4.group(1))
print('result5', result5.group(1))

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)
