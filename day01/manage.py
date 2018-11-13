# -*- coding: utf-8 -*-
# 导包
# from flask import Flask, render_template
from flask_script import Manager
# 实例化Flask
# app = Flask(__name__)
from myapp import create_app

app = create_app()
# 实例化manager
manager = Manager(app=app)

# 注册路由
# @app.route('/')
# 处理函数
# def hello_world():
#     return '<h1>Hello World!</h1>'
#
# @app.route("/index01")
# def index():
#     return render_template("one.html",msg="好玩",data="休息")

# 主函数
if __name__ == '__main__':
    # 启动Flask服务
    # app.run(
    #     host="0.0.0.0.",
    #     port=12349,
    #     debug=True
    # )
    manager.run()