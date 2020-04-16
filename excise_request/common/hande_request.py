"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/11 15:42
E-mail  : 506615839@qq.com
File    : hander_request.py
============================
"""
import requests


class HandleRequest:
    '''使用token鉴权的接口，使用这个类去发送请求'''
    def send(self, url, method, data=None, json=None, params=None, headers=None):
        # 将方法转化为小写
        method=method.lower()
        if method == 'post':
            return requests.post(url=url, json=json, data=data, headers=headers)
        elif method == 'patch':
            return requests.patch(url=url, json=json, data=data, headers=headers)
        elif method == 'get':
            return requests.post(url=url, params=params)


class HandeSession:
    '''使用session鉴权的接口，使用这个类发送请求'''
    def __init__(self):
        self.se=requests.session()

    def send(self, url, method, data=None, json=None, params=None, headers=None):
        # 将方法转化为小写
        method=method.lower()
        if method == 'post':
            return self.se.post(url=url, json=json, data=data, headers=headers)
        elif method == 'patch':
            return self.se.post(url=url, json=json, data=data, headers=headers)
        elif method == 'get':
            return self.se.post(url=url, params=params, headers=headers)





if __name__ == '__main__':
    login_url = 'http://api.lemonban.com/futureloan/member/login'
    # 登录数据
    data = {'mobile_phone': '13641878150',
            'pwd': '12345678'
            }
    headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}

    http=HandleRequest()
    res=http.send(url=login_url,method='POST',json=data,headers=headers)
    print(res.json())