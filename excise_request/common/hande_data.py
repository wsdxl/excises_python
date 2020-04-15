"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/14 23:13
E-mail  : 506615839@qq.com
File    : hande_data.py
============================
"""
import re
from common.read_conf import conf

class CaseData:
    '''专门用来保存一些要替换的数据'''
    member_id=""


def replace_data(data):
    r=r='#(.+?)#'
    # 判断是否有要替换的数据
    while re.search(r,data):
        # 匹配出第一个要替换的数据
        res=re.search(r,data)
        #提取待替换的内容
        item=res.group()
        #提取替换内容中的数据项
        key=res.group(1)
        try:
            # 根据替换内容中的数据项去配置文件中找到对应的的内容，进行替换
            data=data.replace(item,conf.get('env',key))
        except :

            data = data.replace(item, getattr(CaseData,str(key)))
    # 返回替换好的数据
    return data