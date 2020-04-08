"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/8 7:19
E-mail  : 506615839@qq.com
File    : 创建日志收集器.py
============================
"""
import logging

mylog=logging.getLogger()
mylog.setLevel('DEBUG')

logging.debug('这是DEBUG等级信息')
logging.info('这是INFO等级信息')
logging.warning('这是WARNING等级信息')
logging.error('这是ERROR等级信息')
logging.critical('这是CRITICAL等级信息')
