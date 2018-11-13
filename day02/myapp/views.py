from flask import Blueprint, session, render_template
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

@blue.route('/index')
def index():
    import os
    # 获得当前程序运行所在目录
    root = os.path.dirname(__file__)
    # 拼接文件的路径
    file_path = os.path.join(root,'templates','index.html')
    f = open(file_path,'r')
    template = Template(f.read())
    html = template.render()
    return html

@blue.route('/block')
def my_block():
    return render_template('test.html')

@blue.route('/my_marco')
def my_marco():
    data = ['python','php','C','C++']
    return render_template('my_marco.html',data=data)

@blue.route('/for_demo')
def for_demo():
    data = ['python','php','C','C++']
    return render_template('fordemo.html',data=data)