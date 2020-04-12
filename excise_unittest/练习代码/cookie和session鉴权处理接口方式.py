"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/11 15:08
E-mail  : 506615839@qq.com
File    : cookie和session鉴权处理接口方式.py
============================
"""
import requests
# 老版的前程贷登录接口
login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
login_data={
    'mobilephone':'13641878150',
    'pwd':'123456'
}
# 创建一个session对象：能够自动记录上一次请求中的cookie信息
se=requests.session()
r=se.post(url=login_url,data=login_data)
res=r.json()
# print(res)

# 老板前程贷充值接口
recharge_url="http://test.lemonban.com/futureloan/mvc/api/member/recharge"
recharge_data={
    'mobilephone':'13641878150',
    'amount':2000
}

res2=se.post(url=recharge_url,data=recharge_data)
print(res2.json())