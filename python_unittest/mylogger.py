"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/8 7:53
E-mail  : 506615839@qq.com
File    : mylogger.py
============================
"""
import logging

def my_logger(logname,filename):

    # 自定义名字为python的日志收集器
    mylog = logging.getLogger(logname)
    # 设置日志收集器等级为debug等级
    mylog.setLevel('DEBUG')

    # 创建输出渠道
    # 1、控制台输出渠道
    sh = logging.StreamHandler()
    # 设置控制台输出渠道的等级
    sh.setLevel('INFO')
    # 将控制台输出渠道绑定到日志收集器上
    mylog.addHandler(sh)

    # 2、日志输出渠道
    fh = logging.FileHandler(filename, encoding='utf8')
    # 设置控制台输出渠道的等级
    fh.setLevel('DEBUG')
    # 将控制台输出渠道绑定到日志收集器上
    mylog.addHandler(fh)

    # 创建日志收集器格式
    formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
    # 将格式绑定到输入渠道上
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    return mylog

mylog=my_logger('python','log.log')


mylog.debug("这个是自己记录了的debug等级的日志")
mylog.info("这个是自己记录了的info等级的日志")
mylog.warning("这个是自己记录了的warning等级的日志")
mylog.error("这个是自己记录了的error等级的日志")
mylog.critical("这个是自己记录了的critical等级的日志")