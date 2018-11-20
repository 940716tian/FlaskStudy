from flask import Flask
from myapp.ext import init_ext
from myapp.settings import conf
from myapp.urls_apis_v1 import init_api
from myapp.views import init_blue


def create_app(env_name):
    # 做简单的检验
    if not env_name in conf.keys():
        raise Exception("你的环境名有问题")
    app = Flask(__name__)
    # 各种配置
    app.config.from_object(conf.get(env_name))
    # print(conf.get(env_name))
    # 注册各种第三方的插件
    init_ext(app)
    # 注册蓝图
    init_blue(app)

    init_api(app)
    return app