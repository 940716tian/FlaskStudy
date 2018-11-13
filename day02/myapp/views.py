from flask import Blueprint, session
from jinja2 import Template

blue = Blueprint("day02",__name__)

@blue.route('/set')
def set_session():
    session['name'] = 'tom'
    return "OK"

@blue.route('/get')
def get_session():
    res = session.get('name','游客')
    return str(res)

@blue.route('index')
def index():
    template = Template("<h1>呵呵呵</h1>")
    html = template.render()
    return html
