#!/usr/bin/python
# coding:utf-8

"""
@author: zyc
@contact: xx@xx.com
@software: PyCharm
@file: toutiao.py
@time: 2018/9/9 17:26
"""
from multiprocessing.pool import Pool

from unit6_ajax.toutiao.toutiao_image import get_images, image_save
from unit6_ajax.toutiao.toutiao_spider import get_page


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        image_save(item)


GROUP_START = 1
GROUP_END = 20


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
