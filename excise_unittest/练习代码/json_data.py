"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/11 14:57
E-mail  : 506615839@qq.com
File    : json_data.py
============================
"""
import json
data = {"name":"musen","id":18,"msg":None}

json_data = '{"name":"musen","id":19,"msg":null}'

# 将json字符串转化成python中的字典格式
r=json.loads(json_data)
# print(r)

# 将python中字典格式的数据转化成json字符串格式
r1=json.dumps(data)
print(r1,type(r1))