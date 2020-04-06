"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/6 17:36
E-mail  : 506615839@qq.com
File    : test_cases.py
============================
"""
import unittest
from register import register
from login import login_check


class Test_Register(unittest.TestCase):

    def __init__(self, methodName, data, expected):
        super().__init__(methodName)
        self.data = data
        self.expected = expected

    def test_register(self):
        # 一、准备用例数据
        # 1、用例参数
        data = self.data
        # 2、预期结果
        expected = self.expected
        # 二、执行功能函数
        result = register(*data)
        print('result:', result)
        # 三、比对预期结果和实际结果
        self.assertEqual(result, expected)


class TestLogin(unittest.TestCase):

    def __init__(self, methodName, data, expected):
        super().__init__(methodName)
        self.data = data
        self.expected = expected

    def test_login(self):
        pass
        # 准备测试数据
        data = self.data
        expected = self.expected
        # 执行功能函数
        result = login_check(*data)
        # 比对预期结果和实际结果
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
