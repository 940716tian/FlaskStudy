from flask import Blueprint

blue = Blueprint("day04",__name__)

def init_blue(app):
    app.register_blueprint(blue)



