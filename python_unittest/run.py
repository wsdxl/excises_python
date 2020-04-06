"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/6 17:55
E-mail  : 506615839@qq.com
File    : run.py
============================
"""
import unittest
from readexcel import ReadExcel
# import test_cases
from HTMLTestRunnerNew import HTMLTestRunner



# 第一步： 创建测试套件
suite=unittest.TestSuite()
# 第一步：创建加载对象，添加用例
loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_cases))

# 添加注册测试数据
from test_cases import Test_Register
excel=ReadExcel('cases.xlsx','register')
datas=excel.read_excel()

for item in datas:
    case=Test_Register('test_register',eval(item['data']),eval(item['expected']))
    suite.addTest(case)

# 添加登录测试数据
from test_cases import TestLogin
excel1=ReadExcel('cases.xlsx','login')
cases=excel1.read_excel()
for i in cases:
    case=TestLogin('test_login',eval(i['data']),eval(i['expected']))
    suite.addTest(case)
# 第三步：生成测试报告

with open('report.html','wb') as fb:
    runner=HTMLTestRunner(stream=fb,
                   title='测试注册函数',
                   description='复习',
                   tester='dxl')

    runner.run(suite)


