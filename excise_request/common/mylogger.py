"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/8 7:53
E-mail  : 506615839@qq.com
File    : mylogger.py
============================
"""
import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
from common.read_conf import conf
from common.contants import LOG_DIR
import os


level=conf.get('logging','level')
f_level=conf.get('logging','f_level')
s_level=conf.get('logging','s_level')
filename=conf.get('logging','filename')
#获取日志文件的绝对路径
log_path=os.path.join(LOG_DIR,filename)


def my_logger():

    # 自定义名字为python的日志收集器
    mylog = logging.getLogger('python')
    # 设置日志收集器等级为debug等级
    mylog.setLevel(level)

    # 创建输出渠道
    # 1、控制台输出渠道
    sh = logging.StreamHandler()
    # 设置控制台输出渠道的等级
    sh.setLevel(s_level)
    # 将控制台输出渠道绑定到日志收集器上
    mylog.addHandler(sh)

    # 2、日志输出渠道
    # fh = logging.FileHandler(filename, encoding='utf8')

    # 按文件大小进行轮转

    fh=RotatingFileHandler(log_path,maxBytes=1024*1024*20,backupCount=3,encoding='utf8')

    # # 按时间进行轮转
    # fh=TimedRotatingFileHandler('test.log',when='S',interval=1,backupCount=7,encoding='utf8')
    # 设置控制台输出渠道的等级
    fh.setLevel(f_level)
    # 将控制台输出渠道绑定到日志收集器上
    mylog.addHandler(fh)

    # 创建日志收集器格式
    formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
    # 将格式绑定到输入渠道上
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    return mylog

mylog=my_logger()


# mylog.debug("这个是自己记录了的debug等级的日志")
# mylog.info("这个是自己记录了的info等级的日志")
# mylog.warning("这个是自己记录了的warning等级的日志")
# mylog.error("这个是自己记录了的error等级的日志")
# mylog.critical("这个是自己记录了的critical等级的日志")