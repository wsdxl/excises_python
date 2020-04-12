"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/9 8:21
E-mail  : 506615839@qq.com
File    : read_conf.py
============================
"""
from configparser import ConfigParser
from common.contants import CONF_DIR
import os

class MyConf(ConfigParser):

    def __init__(self,filename,encoding='utf8'):
        super().__init__()
        self.filename=filename
        self.encoding=encoding
        self.read(filename,encoding)

    def write_conf(self,section,option,value):
        self.set(section,option,value)
        self.write(open(self.filename,'w',encoding=self.encoding))

# 获取配置文件的绝对路径
conf_path=os.path.join(CONF_DIR,'conf.ini')
conf=MyConf(conf_path)
if __name__ == '__main__':
    url=conf.get('env','url')+'/member/register'
    print(url)