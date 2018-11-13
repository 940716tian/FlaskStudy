from flask import Blueprint, session, render_template
from jinja2 import Template
from myapp.models import db, Person

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

@blue.route('/tags')
def tags():
    my_str = "hello"
    html_str = "<h1>the end is good if not good it's not end</h1>"
    return render_template("filter_tags.html",data=my_str,html_str=html_str,my_arr=[1,3,2,6,5])

@blue.route('/create')
def create_db():
    db.create_all()
    return "创建完毕"

@blue.route('/drop')
def drop_db():
    db.drop_all()
    return "跑路"

@blue.route('/create_data')
def create_user():
    # 创建数据
    # u = Person(
    #     name="张三"
    # )
    # db.session.add(u)
    # db.session.commit()

    # 批量创建
    persons = []
    for i  in range(10):
        u = Person(name="张四"+str(i))
        persons.append(u)
    # 批量写到数据库
    db.session.add_all(persons)
    db.session.commit()
    return "创建完毕"

@blue.route('/get_users')
def get_users():
    # 查询数据
    res = Person.query.all()
    for i in res:
        print(i.name)
    return "OK"

