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
from readexcel import ReadExcel
from ddt import ddt, data


@ddt
class Test_Register(unittest.TestCase):
    excel = ReadExcel('cases.xlsx', 'register')
    register_data = excel.read_excel()

    @data(*register_data)
    def test_register(self, case):
        # 1、准备测试数据
        case_data = eval(case['data'])
        expected = eval(case['expected'])
        case_id = case['case_id']
        # 2、执行功能函数
        result = register(*case_data)

        # 3、比对预期结果与实际结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            self.excel.write_excel(row=case_id+1,column=5,value='未通过')
            raise e
        else:
            self.excel.write_excel(row=case_id + 1, column=5, value='通过')


@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel('cases.xlsx', 'login')
    login_data = excel.read_excel()

    @data(*login_data)
    def test_login(self, case):
        # 1、准备测试数据
        case_data = eval(case['data'])
        expected = eval(case['expected'])
        case_id = case['case_id']
        # 2、执行功能函数
        result = login_check(*case_data)

        # 3、比对预期结果与实际结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            self.excel.write_excel(row=case_id + 1, column=5, value='未通过')
            raise e
        else:
            self.excel.write_excel(row=case_id + 1, column=5, value='通过')


if __name__ == '__main__':
    unittest.main()
