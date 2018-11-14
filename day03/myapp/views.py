from flask import Blueprint, request, render_template,jsonify
from sqlalchemy import or_, and_, not_

from myapp.models import *
# from myapp.ext import db

blue = Blueprint("day03",__name__)

def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/create_dog')
def create_dog():
    # 批量创建
    dogs = []
    for i in range(50):
        dog = Dog()
        dog.name = "泰迪" + str(i+1)
        dog.place = "杭州{num}".format(num=i+1)
        dogs.append(dog)
    # 添加到数据库的session
    db.session.add_all(dogs)
    # 写入数据库
    db.session.commit()
    return "狗已入户"

@blue.route('/del/<int:id>')
def del_dog(id):
    dog = Dog.query.filter_by(id=id).first_or_404()
    # print(dog)
    # print(type(dog))
    # 删除数据
    db.session.delete(dog)
    db.session.commit()
    return "OK"

@blue.errorhandler(404)
def my_404(e):
    return "资源不存在"

@blue.route('/get_dogs/')
def get_dogs():
    params = request.args
    # ID大于20
    # dogs = Dog.query.filter(Dog.id.__gt__(20))

    # name=泰迪9
    # dogs = Dog.query.filter(Dog.name=="泰迪9")

    # 获取泰迪包含34的泰迪狗
    # dogs = Dog.query.filter(Dog.name.contains("34"))

    # 获取ID是9,10,11的数据
    # dogs = Dog.query.filter(Dog.id.in_([9,10,11]))

    # 获取以4结尾的数据
    dogs = Dog.query.filter(Dog.name.like('%4_'))

    # get 只能通过主键去搜索
    # dog = Dog.query.get_or_404(1)
    # print(dog)

    # 跳过N条数据 offset(N)
    # dogs = dogs.offset(3)

    # 最多取N条
    # dogs = dogs.limit(6)

    # 联合使用 跳过N条数据 最多取N个数据 offset(N).limit(N)
    # dogs = dogs.offset(2).limit(3)

    # 要先排序才能再去使用limit 或者 offset
    dogs = dogs.order_by("-id").offset(2)
    return render_template('datas.html',dogs=dogs)

@blue.route('/page/')
def get_page_data():
    # 获取数据集
    dogs = Dog.query.filter(Dog.id.__gt__(1))
    # 当前页码
    current_page = int(request.args.get("page",1))
    # 每一页放多少数据
    per_page = int(request.args.get("per",20))
    # 获得分页对象
    paginates = dogs.paginate(current_page,per_page)

    # datas = dogs.offset((current_page-1)*per_page).limit(per_page)
    # return render_template("datas.html",dogs=datas)

    # return render_template("datas.html",dogs=paginates.items)

    dogs_data = [i.to_dict() for i in paginates.items]
    data = {
        "code":1,
        "msg":"OKKK",
        "data":{
            "dogs":dogs_data,
            "pages":paginates.pages,
            "prev_num":paginates.prev_num,
            "has_next":paginates.has_next,
            "next_num":paginates.next_num,
            "current_page":paginates.page
        }
    }
    return jsonify(data)

@blue.route('/query')
def my_query():
    # or_(条件1，条件2，条件N）
    # and_(条件1，条件2，条件N）
    # not_(条件1，条件2，条件N）
    # dogs = Dog.query.filter(or_(Dog.name.contains("尼克"),Dog.name.contains("4")))
    dogs = Dog.query.filter(and_(Dog.name.contains("泰迪"),Dog.name.contains("5")))
    # dogs = Dog.query.filter(not_(Dog.name.contains("尼克")))
    return render_template("datas.html",dogs=dogs)

@blue.route('/get_grade/<int:sid>')
def get_grade(sid):
    # 先查学生
    stu = Stu.query.get(sid)
    # 通过学生的grade_id获取班级信息
    # grade = Grade.query.get(stu.grade_id)
    grade = stu.grade # grade 就是我们在模型relationship里指定的那个backref 对应的值

    return grade.name

@blue.route('/get_stu/<int:gid>')
def get_stu(gid):
    # 通过直接查询获得数据
    # stu = Stu.query.filter(Stu.grade_id==gid)

    # 通过关系获得数据
    stu = Grade.query.get(gid).stus # 直接访问stus
    for i in stu:
        print(i)
    return "ok"

@blue.route('/create_my_data')
def create_my_data():
    tag1 = Tag(title="python")
    tag2 = Tag(title="java")

    db.session.add_all([tag1,tag2])
    db.session.commit()

    book1 = Book(name="西游记")
    book2 = Book(name="红楼梦")
    # 追加的方式
    book1.tags.append(tag1)
    book2.tags.append(tag2)
    # 直接复制的方式
    book2.tags = [tag1,tag2]
    # 写到数据库
    db.session.add_all([book1,book2])
    db.session.commit()
    return "OK"

@blue.route('/get_book/<int:t_id>')
def get_book_by_tag(t_id):
    # 查tag
    tag = Tag.query.get(t_id)
    books = tag.books
    for i in books:
        print(i.name)
    return "OK"

@blue.route('/get_tag/<int:b_id>')
def get_tag_by_book(b_id):
    book = Book.query.get(b_id)
    tags = book.tags
    for i in tags:
        print(i.title)
    return "OJBK"
