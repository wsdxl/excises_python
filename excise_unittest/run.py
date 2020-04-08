"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/6 17:55
E-mail  : 506615839@qq.com
File    : run.py
============================
"""
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner

#第一步：创建测试套件
suite=unittest.TestSuite()

#第二步：加载测试用例到测试套件中
loader=unittest.TestLoader()
suite.addTest(loader.discover(r'F:\project\excise_unittest\testcases'))

# 第三步：创建启动程序
report_path=r'F:\project\excise_unittest\reports\report.html'
with open(report_path,'wb') as f:
    runner=HTMLTestRunner(stream=f,
                   title='练习单元测试框架unittest',
                   description='主要用单元测试框架搭建接口自动化测试框架',
                   tester='dxl'
                   )
    # 运行程序
    runner.run(suite)


