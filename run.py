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
import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# 常量设置
basedir = os.path.abspath(os.path.dirname(__name__))
ADMIN_USER_ROOT = "admin"
ADMIN_USER_PASS = "sunriseme"

# 初始化app
db_file_name = "sqlite.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(basedir, db_file_name))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app = Flask(__name__)


# 数据库模型
class User(db.Model):
    """
    用户表
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.id},{self.username},{self.email}>'


class ShadowConf(db.Model):
    """
    shadowsocks 配置表
    """
    #  主键id
    id = db.Column(db.Integer, primary_key=True)
    # 用户id
    user_id = db.Column(db.Integer, nullable=False)


# 是否初始化数据库
db_file_dir = os.path.join(basedir, db_file_name)
# F:\pycharmProjects\managers\sqlite.db
# print(db_file_dir)
if not os.path.exists(db_file_dir):
    db.create_all()
else:
    pass


# 视图集合
@app.route('/')
def index():
    return 'Managers is here'


@app.route("/admin")
def admin():
    return "Admin is here"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
