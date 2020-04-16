"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/16 23:42
E-mail  : 506615839@qq.com
File    : test_invest.py
============================
"""
import unittest
import os
import jsonpath
from library.ddt import ddt,data
from common.readexcel import ReadExcel
from common.contants import DATA_DIR
from common.read_conf import conf
from common.hande_data import CaseData,replace_data
from common.hande_request import HandleRequest


data_path=os.path.join(DATA_DIR,'cases.xlsx')

@ddt
class TestInvest(unittest.TestCase):
    excel=ReadExcel(data_path,'invest')
    cases=excel.read_excel()
    http=HandleRequest()

    @data(*cases)
    def test_invest(self,case):
        pass
        # 准备用例数据
        url=conf.get('env','url')+case['url']
        # 测试数据
        case['data']=replace_data(case['data'])
        data=eval(case['data'])
        # 请求方法
        method=case['method']
        # 请求头
        if case['interface']!='login':
            headers=eval(conf.get('env','headers'))
            headers['Authorization']=getattr(CaseData,'token_data')
        # 预期结果
        expected=eval(case['expected'])
        # 行号
        row=case['case_id']+1

        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()

        #提取member_id和token
        if case['title']=='管理员正常登录' and res['msg']=='OK':
            admin_member_id=jsonpath.jsonpath(res,'$..id')[0]
            setattr(CaseData,'admin_member_id',str(admin_member_id))
            token_type=jsonpath.jsonpath(res,'$..token_type')[0]
            token = jsonpath.jsonpath(res, '$..token')[0]
            token_data=token_type+' '+token



        # 断言