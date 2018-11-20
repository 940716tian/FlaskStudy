from flask_restful import fields

# 准备输出字段
one_fields = {
    "id":fields.Integer,
    # "title":fields.String
    "name":fields.String(attribute="title"), # 起别名
    "content":fields.String,
    "hehe":fields.String(default="lalala")
}

two_fields = {
    "name":fields.String(default="Jane"),
    # 列表 里面是字符串
    'hobby':fields.List(fields.String)
}

three_fields = {
    'code':fields.Integer(default=1),
    'msg':fields.String(default="OK"),
    'data':fields.Nested(one_fields)
}

four_fields = {
    'code': fields.Integer(default=1),
    'msg': fields.String(default="OK"),
    'data':fields.List(fields.Nested(one_fields))
}

four_fields = three_fields # 赋值
four_fields['data'] = fields.List(fields.Nested(one_fields)) # 修改
four_fields.pop('msg') # 删除
four_fields['hehe'] = "ajdfnasj" # 添加