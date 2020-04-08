"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/8 23:25
E-mail  : 506615839@qq.com
File    : testcase.py
============================
"""
import unittest
from library.ddt import ddt,data
from common.readexcel import ReadExcel
from login_register.register import register
from login_register.login import login_check
from common.mylogger import mylog

@ddt
class TestRegister(unittest.TestCase):
    excel=ReadExcel(r'F:\project\excise_unittest\data\cases.xlsx','register')
    register_data=excel.read_excel()

    @data(*register_data)
    def test_register(self,case):
        # 准备测试数据
        register_data=eval(case['data'])
        expected=eval(case['expected'])
        row=case['case_id']+1
        # 执行功能函数
        result=register(*register_data)

        # 比对预期结果与实际结果
        try:
            self.assertEqual(expected,result)
        except AssertionError as e:
            self.excel.write_excel(row=row,column=5,value='未通过')
            mylog.info('用例{}---->测试未通过'.format(case['title']))
            mylog.error(e)
            raise e
        else:
            self.excel.write_excel(row=row,column=5,value='通过')
            mylog.info('用例{}---->测试已通过'.format(case['title']))

@ddt
class TestLogin(unittest.TestCase):
    excel=ReadExcel(r'F:\project\excise_unittest\data\cases.xlsx','login')
    login_data=excel.read_excel()

    @data(*login_data)
    def test_login(self,case):
        # 准备测试数据
        login_data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        # 执行功能函数
        result =login_check (*login_data)

        # 比对预期结果与实际结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            self.excel.write_excel(row=row, column=5, value='未通过')
            mylog.info('用例{}---->测试未通过'.format(case['title']))
            mylog.error(e)
            raise e
        else:
            self.excel.write_excel(row=row, column=5, value='通过')
            mylog.info('用例{}---->测试已通过'.format(case['title']))
