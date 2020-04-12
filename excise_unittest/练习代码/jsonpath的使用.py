"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/11 14:21
E-mail  : 506615839@qq.com
File    : jsonpath的使用.py
============================
"""
import requests
import jsonpath
# 登录接口
# url地址
login_url='http://api.lemonban.com/futureloan/member/login'
# 登录数据
data={'mobile_phone':'13641878150',
      'pwd':'12345678'
      }
# 登录请求头
headers = {"X-Lemonban-Media-Type": "lemonban.v2","Content-Type": "application/json"}
# 发起请求，获取响应
r=requests.post(url=login_url,json=data,headers=headers)
res=r.json()
# 提取id
id=jsonpath.jsonpath(res,'$..id')[0]
# 提取token类型
token_type=jsonpath.jsonpath(res,'$..token_type')[0]
# 提取token
token=jsonpath.jsonpath(res,'$..token')[0]
# 拼接token_data
token_data=token_type+' '+token
print(id)
print(token_data)

# 充值接口
header_token = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json",
    "Authorization":token_data
}

recharge_url='http://api.lemonban.com/futureloan/member/recharge'
data={
    'member_id':id,
    'amount':2000
}
res1=requests.post(url=recharge_url,json=data,headers=header_token)
res2=res1.json()
print(res2)