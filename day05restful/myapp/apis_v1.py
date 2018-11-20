from flask import request
from flask_restful import Resource, marshal_with
from fields_apis_v1 import *
from myapp.args_apis_v1 import my_params, two_args, three_args
from myapp.models import News


class NewsOneApi(Resource):

    @marshal_with(one_fields)
    def get(self,*args,**kwargs):
        id = int(request.args.get("id"))
        news = News.query.get_or_404(id)
        return news

class NewsTwoApi(Resource):

    @marshal_with(two_fields)
    def get(self,*args,**kwargs):
        hobby = ['抽烟','喝酒','拖车']

        return {'hobby':hobby,'name':'hehe','age':2}

class NewsThreeApi(Resource):

    @marshal_with(three_fields)
    def get(self,**kwargs):
        id = kwargs.get("id")
        print(id,type(id))
        news = News.query.get_or_404(id)
        return {"data":news}

class FourApi(Resource):

    @marshal_with(four_fields)
    def get(self,page,per_page):
        # 分页实现
        datas = News.query.paginate(page,per_page,error_out=FloatingPointError)
        return {"code":2,"data":datas.items}

class FiveApi(Resource):

    def get(self):
        my_args = my_params.parse_args()
        print(my_args)
        print(my_args.get("hobby"))
        return {'msg':'ok'}

class SixApi(Resource):

    def get(self):
        args = two_args.parse_args()
        print(args)
        return {'msg':'ok'}

    def post(self):
        args = two_args.parse_args()
        print(args)
        return {'ok':1}

class SevenApi(Resource):

    def get(self):
        my_args = three_args.parse_args()
        print(my_args)
        return {'msg':'ok'}

