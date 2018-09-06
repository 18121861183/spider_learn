#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: yaochen.zhao@colasoft.com.cn
@software: PyCharm
@file: 21_request_cookie.py
@time: 2018/9/6 15:48
"""
import requests

# 获取cookie信息
# r = requests.get("https://www.zhihu.com")
# print(r.cookies)
#
# for key, value in r.cookies.items():
#     print(key + '=' + value)

# 已登录网页cookie
headers = {
    'Cookie': 'BDUSS=pneUVxaUNrRGFqZ1dhUWE1MWJFbXdOT3lMTVJpZzJ1bG12YUdlbHpNcGU0aHhiQVFBQUFBJCQAAAAAAAAAAAEAAAB8aBscMTYwMDY1MDk1MwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF5V9VpeVfVaWW; BD_UPN=12314753; BIDUPSID=0FA0ABD44592505BAF9AAE15D4A12085; BAIDUID=7007973DA92C00A848E54DE1433169F9:FG=1; PSTM=1535952536; delPer=0; BD_HOME=1; H_PS_PSSID=1468_21086_18560_26350_20930',
    'Host': 'www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get('https://www.baidu.com', headers=headers)
print(r.text)
