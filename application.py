#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: application.py
@time: 2019/2/25 23:52
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Managers is here'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
