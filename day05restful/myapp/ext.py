from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
def init_ext(app):

    # db绑定
    db.init_app(app)

    # 实例化migrate
    migrate = Migrate(app=app,db=db)







