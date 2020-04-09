"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/9 8:21
E-mail  : 506615839@qq.com
File    : read_conf.py
============================
"""
from configparser import ConfigParser

class MyConf(ConfigParser):

    def __init__(self,filename,encoding='utf8'):
        super().__init__()
        self.filename=filename
        self.encoding=encoding
        self.read(filename,encoding)



    def write_conf(self,section,option,value):
        self.set(section,option,value)
        self.write(open(self.filename,'w',encoding=self.encoding))

conf=MyConf(r'F:\excises_python\excise_unittest\conf\conf.ini')
