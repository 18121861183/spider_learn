# -*- coding:utf-8 -*-
from urllib.parse import urlparse

'''
    url解析： scheme 协议 ； netloc 域名； path , 分号；前代表参数, query代表查询参数， fragment页面锚点
    <class 'urllib.parse.ParseResult'> ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
'''
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

'''
    URL不带HTTPS，则结果解析会出现偏差
    ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=S', fragment='comment')
'''
result1 = urlparse('www.baidu.com/index.html;user?id=S#comment', scheme='https')
print(result1)

"""
    scheme代表协议，协议依照URL解析结果为准
    ParseResult(scheme='https', netloc='www .baidu. com', path='/index .html', params='user', query='id=S ', fragment='com ment')
"""
result2 = urlparse('https://www.baidu.com/index.html;user?id=S#comment', scheme='http')
print(result2)

'''
    allow_fragments=False 代表不解析锚点; query参数会出现异常
    ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=S#comment', fragment='')
'''
result3 = urlparse('https://www.baidu.com/index.html;user?id=S#comment', scheme='http', allow_fragments=False)
print(result3)

'''
    allow_fragments=False 代表不解析锚点; path参数会出现异常
    ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html#comment', params='', query='', fragment='')
'''
result4 = urlparse('https://www.baidu.com/index.html#comment', scheme='http', allow_fragments=False)
print(result4)

'''

'''
result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result. scheme, result[0], result. netloc, result[1], sep='\n')
