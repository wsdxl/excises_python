"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/9 7:28
E-mail  : 506615839@qq.com
File    : 配置文件操作.py
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


if __name__ == '__main__':
    conf=MyConf('conf.ini')
    c=conf.get('logging','set_level')
    print(c)