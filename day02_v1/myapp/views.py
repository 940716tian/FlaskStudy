from flask import Blueprint
# from myapp.ext import db

blue = Blueprint("app",__name__)

def init_blue(app):
    app.register_blueprint(blue)