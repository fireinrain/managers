#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: application.py
@time: 2019/2/25 23:52
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2019, Node Supply Chain Manager Corporation Limited.
"""
from application import app


@app.route('/')
def index():
    return 'Managers is here'
