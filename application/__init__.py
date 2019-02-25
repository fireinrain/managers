#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: __init__.py
@time: 2019/2/26 0:05
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2019, Node Supply Chain Manager Corporation Limited.
"""
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app = Flask(__name__)
