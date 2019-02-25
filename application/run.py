#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: run.py
@time: 2019/2/26 0:07
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2019, Node Supply Chain Manager Corporation Limited.
"""

from application import app

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
