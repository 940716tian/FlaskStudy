from flask import Flask
from .views import blue

def create_app():
    # 创建APP flask的实例
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'guangfangyidiande'
    # 注册蓝图
    app.register_blueprint(blue)
    return app