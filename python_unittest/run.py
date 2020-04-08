"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/6 17:55
E-mail  : 506615839@qq.com
File    : run.py
============================
"""
import unittest
import test_cases
from HTMLTestRunnerNew import HTMLTestRunner



# 第一步： 创建测试套件
suite=unittest.TestSuite()
# 第二步：创建加载对象，添加用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_cases))


# 第三步：生成测试报告

with open('report.html','wb') as fb:
    runner=HTMLTestRunner(stream=fb,
                   title='测试注册函数',
                   description='复习',
                   tester='dxl')

    runner.run(suite)


