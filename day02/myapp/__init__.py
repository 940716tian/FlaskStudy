from flask import Flask
from myapp.models import db
from .views.views import blue
from flask_session import Session
from redis import StrictRedis

def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "qwertyuiop"
    app.config["SESSION_TYPE"] = "redis" # 指定session存储方案
    app.config["SESSION_KEY_PREFIX"] = "myapp:" # 设置缓存开头
    app.config['SESSION_REDIS'] = StrictRedis(host='127.0.0.1',db=5) #定制化的将session存到Redis中

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://xiao_hu:123@127.0.0.1:3306/hzfl02"
    # 实例化session
    sess = Session()
    sess.init_app(app)

    # 注册蓝图
    app.register_blueprint(blue)
    # 与app绑定
    db.init_app(app)
    return app