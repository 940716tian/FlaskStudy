from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache
from myapp.settings import CACHES
from flask_restful import Api

api = Api()
db = SQLAlchemy()
bs = Bootstrap()
cache = Cache(config=CACHES.get("default"))
def init_ext(app):

    # 实例化
    se = Session()
    # 绑定app
    se.init_app(app)

    # db绑定
    db.init_app(app)

    # 实例化migrate
    migrate = Migrate(app=app,db=db)

    bs.init_app(app)

    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    cache.init_app(app)

    api.init_app(app)




