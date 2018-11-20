from flask import Blueprint, render_template, request, jsonify
from .models import News
from .ext import db, cache, api
from flask_restful import Resource

blue = Blueprint("day04",__name__)

def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/news',methods=['GET','POST','PUT','DELETE'])
def news_api():
    if request.method == "GET":
        # 获取数据
        id = int(request.args.get("id",1))
        news = News.query.get_or_404(id)
        result = {
            'code':1,
            'msg':"OKKK",
            'data':news.to_dict()
        }
        return jsonify(result)
    elif request.method == "POST":
        # 创建数据
        params = request.form
        title = params.get("title")
        content = params.get("content")

        news = News(
            title=title,
            content=content
        )
        db.session.add(news)
        db.session.commit()
        result = {
            'code': 1,
            'msg': "OKKK",
            'data': news.to_dict()
        }
        return jsonify(result),201
    elif request.method == "PUT":
        # 修改数据
        params = request.form
        id = int(params.get("id"))
        # 知道改谁
        news = News.query.get_or_404(id)

        # 能解析到 就用解析到的数据 如果不能 就用原来的数据
        title = params.get("title",news.title)
        content = params.get("content",news.content)

        news.title = title
        news.content = content

        db.session.add(news)
        db.session.commit()
        result = {
            'code': 1,
            'msg': "OKKK",
            'data': news.to_dict()
        }
        return jsonify(result), 201
    else:
        # 删除
        id = int(request.form.get("id"))

        news = News.query.get_or_404(id)
        result = {
            'msg': "OKKK",
            'data': news.to_dict()
        }
        db.session.delete(news)
        db.session.commit()
        return jsonify(result),204

class NewsApiTest(Resource):

    def get(self):
        return {'data':'nimadi'}

api.add_resource(NewsApiTest,'/test','/hehe')

