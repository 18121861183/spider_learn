#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 22_request_cookie2.py
@time: 2018/9/6 16:07
"""
import requests
cookies = 'BDUSS=pneUVxaUNrRGFqZ1dhUWE1MWJFbXdOT3lMTVJpZzJ1bG12YUdlbHpNcGU0aHhiQVFBQUFBJCQAAAAAAAAAAAEAAAB8aBscMTYwMDY1MDk1MwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF5V9VpeVfVaWW; BD_UPN=12314753; BIDUPSID=0FA0ABD44592505BAF9AAE15D4A12085; BAIDUID=7007973DA92C00A848E54DE1433169F9:FG=1; PSTM=1535952536; delPer=0; BD_HOME=1; H_PS_PSSID=1468_21086_18560_26350_20930'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('http://www.baidu.com', cookies=jar, headers=headers)
print(r.text)
