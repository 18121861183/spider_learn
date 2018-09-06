# -*- coding:utf-8 -*-
from urllib.parse import urlunparse, urlsplit, urljoin

'''
data组合成URL
'''
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

'''
与urlparse相似，不单独解析params部分
SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='a=6', fragment='comment') http http
'''
result = urlsplit('http://www.baidu.com/index.html;user?a=6#comment')
print(result, result[0], result.scheme)

'''
urlunsplit() 与urlunparse类似，长度必须是5
'''

'''
链接的解析和拼合
'''
print(urljoin(' http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com ', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com ', '?category=2#comment'))
