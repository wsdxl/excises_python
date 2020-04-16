"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/11 21:46
E-mail  : 506615839@qq.com
File    : test.py
============================
"""
import random
from  common.read_conf import conf

# def random_phone():
#     phone='13'
#     for i in range(9):
#         phone+=str(random.randint(0,9))
#     return phone
# phone=random_phone()
# print(phone)

# login_url=conf.get('env','url')+'/member/login'
# print(login_url)

# str1='{"member_id":#member_id#,"amount":200}'
# if '#member_id#' in str1:
#     str1=str1.replace('#member_id#', str(1))
# recharge_data = eval(str1)
# print(recharge_data)

import requests

url='http://api.lemonban.com/futureloan/loan/audit'
data={'loan_id': 81804, 'approved_or_not': True}
headers={"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json","Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjgwMjk0MDYsImV4cCI6MTU4Njk2NTM4NX0.A2qwek6GBH72HkY4EnMXqzoLZEAN5xtx4LCpvoIIFEBpQwsRAJjJWffbg3zbYhEchO7Fd6o22_vdtF4GjKZ7Kg"}
response=requests.patch(url=url,json=data,headers=headers)
res=response.json()
print(res)