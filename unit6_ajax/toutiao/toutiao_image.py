#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: xx@xx.com
@software: PyCharm
@file: toutiao_image.py
@time: 2018/9/9 17:17
"""
import os
import requests
from hashlib import md5


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images is not None and len(images)>0:
                for img in images:
                    yield {
                        'image': img.get('url'),
                        'title': title
                    }


# 图片保存
def image_save(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get('https://'+item.get('image')[2:])
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('already download', file_path)
    except requests.ConnectionError:
        print('save image failed')
