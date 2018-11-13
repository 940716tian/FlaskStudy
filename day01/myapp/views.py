from flask import Blueprint, url_for, redirect, render_template, request, make_response, abort, session

blue = Blueprint("hello",__name__)

@blue.route("/myblue")
def hello_blue_print():
    return "我是蓝图，规划URL"

@blue.route('/param/<int:id>')
def param(id):
    print(id)
    print(type(id))
    return str(id)

@blue.route('/param/<path:my_path>')
def param_path(my_path):
    print(my_path)
    print(type(my_path))

    import uuid
    uuid_val = uuid.uuid4()
    return str(uuid_val)

@blue.route("/params/<uuid:my_uuid>")
def param_uuid(my_uuid):
    print(my_uuid)
    return "OK"

@blue.route("/my_any/<any(a,b,c,'20'):p>",methods=['GET','POST'])
def my_any(p):
    # print(p)
    # url_for("蓝图，函数名")
    # res = url_for("hello.hello_blue_print")
    # 带参数
    res = url_for("hello.param",id=1,name="aha")
    return redirect(res)

@blue.route("/index")
def index():
    return render_template("one.html")

@blue.route('/req',methods=["GET","POST","PUT","DELETE"])
def look_req():
    req = request
    # print(req.method)
    # print(req.path)
    # print(req.url)
    # print(req.args)
    # print(req.form)
    # print(req.base_url)
    # print(dir(req))
    # print("name",req.args.get("name"))
    # print("name",req.args.getlist("name"))
    print('file',req.files)
    print('real files',req.files.get("myfiles"))
    print(dir(req.files))
    return "OK"

@blue.route('/response')
def my_response():
    # response = make_response("hehe",404)
    # return response
    abort(403)  # 主动终止 括号内是状态码
    return "呵呵",500

# 捕获异常
@blue.errorhandler(403)
def handle_403(e):
    print(e)
    return "无权限"

@blue.route('/home')
def home():
    # 通过cookie获取
    uname = request.cookies.get('name')

    # 在session里获取数据
    session_name = session.get('uname')

    # 不确定是否能拿到
    uname = uname if uname else "游客"
    return render_template("home.html",uname=uname)
@blue.route('/login',methods=['GEt','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        # 解析post请求的参数
        name = request.form.get('name')
        #重定向到home
        response = redirect(url_for('hello.home'))

        # 设置session
        session['uname'] = name


        #设置cookie
        response.set_cookie('name',name,max_age=30)
        return response
    else:
        abort(405)

@blue.route('/logout')
def logout():
    # 跳转到home
    response = redirect(url_for('hello.home'))
    # 删除cookie
    response .delete_cookie('name')

    # 删除session
    session.pop('uname')
    return response