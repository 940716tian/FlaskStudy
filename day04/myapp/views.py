from flask import Blueprint, render_template, request, jsonify
from .models import News
from .ext import db, cache

blue = Blueprint("day04",__name__)

def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/create_data')
def create_data():
    datas = []
    for i in range(101):
        tmp = News(
            title="惊喜" + str(i+1) + "哈哈",
            content="惊喜就是没有惊喜，知道不" + str(i+1)
        )
        datas.append(tmp)
    db.session.add_all(datas)
    db.session.commit()
    return "OJBSPBBK"

@blue.route('/')
@cache.cached(timeout=60)
def index():
    # 解析参数
    print("进入函数")
    param = request.args
    page = int(param.get("page",1))
    per_page = int(param.get("per_page",15))

    paginater = News.query.paginate(page,per_page,error_out=False)

    return render_template("index.html",news=paginater.items,pagination=paginater)

@blue.route('/cache')
def my_cache():
    # 先获取ip拼接 我们的key
    ip = request.remote_addr
    key = ip + "day04"
    # 去缓存尝试拿数据
    data = cache.get(key)
    if data:
        print("有数据")
        return jsonify(data)
    else:
        new_data = {
            "code":1,
            "msg":"OKKK",
            "data":"zdvjkadhfvja"
        }
        # 设置缓存
        cache.set(key,new_data,30)
        return jsonify(new_data)

@blue.before_request
def heheda():
    # 反爬 首先检查有没有user_agent 再看IP如果在30访问10次就搞他
    user_agent = request.user_agent
    if not user_agent:
        return jsonify({"code":10000,"msg":"换个网站"},500)
    ip = request.remote_addr
    key = ip + "fanpa"
    times = cache.get(key)
    if not times:
        cache.set(key,1,30)
    else:
        if int(times) >= 3:
            return "nm",404
        else:
            cache.set(key,times+1,30)

