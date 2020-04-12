"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/11 13:26
E-mail  : 506615839@qq.com
File    : requests请求的使用.py
============================
"""
import requests

register_url='http://api.lemonban.com/futureloan/member/register'
data={'mobile_phone':'13641878153',
      'pwd':'12345678',
      'type':1,
      'reg_name':'test8153123456'
      }

headers = {"X-Lemonban-Media-Type": "lemonban.v2","Content-Type": "application/json"}

r=requests.post(url=register_url,json=data,headers=headers)
res=r.content.decode('utf8')
print(res,type(res))