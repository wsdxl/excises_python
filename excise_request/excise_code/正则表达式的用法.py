"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/14 6:50
E-mail  : 506615839@qq.com
File    : 正则表达式的用法.py
============================
"""
import re
from common.read_conf import conf
# # 1.单字符的表示规则
# # .代表匹配除\n以外的任意字符
# re1='.'
# res=re.findall(re1,'f\nrhagdg')
# print(res)

# # []举例一个字符
# re2='[abc]'
# res1=re.findall(re2,'1iugfiSHOIFUOFGIDHFGFD2345a6a78b99cc')
# print(res1)

# # \d表示一个数字
# re3='\d'
# res2=re.findall(re3,'dnmhvvb4567nggn5fgrt44-fblg')
# print(res2)

# # \D 表示非数字
# re4='\D'
# res3=re.findall(re4,'dnmhvvb4567nggn5fgrt44-fblg')
# print(res3)

# # \s：表示一个空白键
# re5 = r"\s"
# res5 = re.findall(re5,"a s d a  9999")
# print(res5)

# # \S：表示一个非空白键
# re6 = r"\S"
# res6 = re.findall(re6,"a s d a  9999")
# print(res6)

# # \w：表示一个单词字符(数字、字母、下划线)
# re6 = r"\w"
# res6 = re.findall(re6,"a s d a ，？“： 99?$%^%!@#@#&^*()99_asjfau")
# print(res6)

# # \W：表示一个非单词字符(不是数字、字母、下划线)
# re7 = r"\W"
# res7 = re.findall(re7,"a98fgjid%^%!@#@#&^*()99_asjfau")
# print(res7)

# data='{"mobile_phone":"#phone#","pwd":"#pwd#"}'
# r='#(.+?)#'
# res=re.search(r,data)
# if res:
#     item=res.group()
#     key=res.group(1)
#     data=data.replace(item,conf.get('env',key))
#     print(data)
class CaseData:
    '''专门用来保存一些要替换的数据'''
    member_id=""
def replace_data(data):
    r=r='#(.+?)#'
    # 判断是否有要替换的数据
    while re.search(r,data):
        # 匹配出第一个要替换的数据
        res=re.search(r,data)
        #提取待替换的内容
        item=res.group()
        #提取替换内容中的数据项
        key=res.group(1)
        try:
            # 根据替换内容中的数据项去配置文件中找到对应的的内容，进行替换
            data=data.replace(item,conf.get('env',key))
        except :

            data = data.replace(item, getattr(CaseData,key))
    # 返回替换好的数据
    return data



data='{"mobile_phone":"#phone#","pwd":"#pwd#","member_id":#member_id#}'
data=replace_data(data)
print(data)