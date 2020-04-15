"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/6 17:55
E-mail  : 506615839@qq.com
File    : run.py
============================
"""
import os
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.contants import REPORT_DIR,CASE_DIR
from common.read_conf import conf
from testcases import test_login,test_recharge,test_withdraw,test_register,test_add,test_audit

#第一步：创建测试套件
suite=unittest.TestSuite()

#第二步：加载测试用例到测试套件中
loader=unittest.TestLoader()
# suite.addTest(loader.discover(CASE_DIR))
suite.addTest(loader.loadTestsFromModule(test_audit))
# 第三步：创建启动程序
report_path=os.path.join(REPORT_DIR,conf.get('report','filename'))
with open(report_path,'wb') as f:
    runner=HTMLTestRunner(stream=f,
                   title=conf.get('report','title'),
                   description=conf.get('report','description'),
                   tester=conf.get('report','tester')
                   )
    # 运行程序
    runner.run(suite)


