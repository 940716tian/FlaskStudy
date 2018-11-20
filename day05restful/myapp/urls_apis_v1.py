from flask_restful import Api
from myapp.apis_v1 import *

# 初始化
api = Api()
# 绑定app
def init_api(app):
    api.init_app(app)

# 注册各种路由
api.add_resource(NewsOneApi,'/newsone')
api.add_resource(NewsTwoApi,'/two')
api.add_resource(NewsThreeApi,'/three/<int:id>')
api.add_resource(FourApi,'/four/<int:page>/<int:per_page>')
api.add_resource(FiveApi,'/five')
api.add_resource(SixApi,'/six')
api.add_resource(SevenApi,'/seven')
