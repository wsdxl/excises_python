"""
============================
Author:柠檬班-木森
Time:2019/11/20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
def login_check(username=None, password=None):
    """
    登录校验的函数
    :param username: 账号
    :param password:  密码
    :return: dict type
    """
    if all([username, password]):
        if username == 'python24' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "mgs": "所有的参数不能为空"}