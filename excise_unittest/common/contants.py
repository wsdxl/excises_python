"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/9 23:11
E-mail  : 506615839@qq.com
File    : contants.py
============================
"""
import os
'''
该模块用来处理整个项目目录的路径
'''

# # 当前文件的绝对路径
# dir=os.path.abspath(__file__)
# print(dir)
# print(__file__)



# 项目目录路径
BASEDIR=os.path.dirname(os.path.dirname(__file__))
# 配置文件路径
CONF_DIR=os.path.join(BASEDIR,'conf')
# 用例数据路径
DATA_DIR=os.path.join(BASEDIR,'data')
# 日志文件路径
LOG_DIR=os.path.join(BASEDIR,'logs')
# 测试报告路径
REPORT_DIR=os.path.join(BASEDIR,'reports')
#测试用例模块路径
CASE_DIR=os.path.join(BASEDIR,'testcases')
