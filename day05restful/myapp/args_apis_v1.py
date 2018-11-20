from flask_restful import reqparse


my_params = reqparse.RequestParser()
my_params.add_argument("name",dest="my_name")
my_params.add_argument("id",type=int,required=True,help='必填字段')
my_params.add_argument('hobby',required=True,action="append") # 解析一个参数多个值

two_args = reqparse.RequestParser()
# 指定解析的位置是form
two_args.add_argument('name',location=['form','args'])

three_args = my_params.copy()
three_args.replace_argument('id',help="我是新的")
three_args.remove_argument("hobby") # 移除
three_args.remove_argument("name") # 移除
three_args.add_argument('age',required=True,type=int)
three_args.add_argument('age',required=True,type=int,choices=[18,19,20])
# 参数值剩下ID age
