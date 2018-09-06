#!/usr/bin/python
# coding:utf-8

"""
@author: Lieb
@contact: xx@xx.com
@software: PyCharm
@file: 30_regex_search.py
@time: 2018/9/6 22:38
"""
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''


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
# search 返回第一个符合条件的匹配目标
results = re.search('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
if results:
    print(results .group(1), results .group(2))
