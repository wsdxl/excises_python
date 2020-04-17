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
from common.mylogger import mylog
from common.hande_db import Hande_DB


data_path=os.path.join(DATA_DIR,'cases.xlsx')

@ddt
class TestInvest(unittest.TestCase):
    excel=ReadExcel(data_path,'invest')
    cases=excel.read_excel()
    http=HandleRequest()
    db=Hande_DB()

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
        headers = eval(conf.get('env', 'headers'))
        if case['interface']!='login':
            headers['Authorization']=getattr(CaseData,'token_data')
        # 预期结果
        expected=eval(case['expected'])
        # 行号
        row=case['case_id']+1

        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()

        #提取member_id和token
        if case['interface']=='login' and res['msg']=='OK':
            member_id=jsonpath.jsonpath(res,'$..id')[0]
            setattr(CaseData,'member_id',str(member_id))
            token_type=jsonpath.jsonpath(res,'$..token_type')[0]
            token = jsonpath.jsonpath(res, '$..token')[0]
            token_data=token_type+' '+token
            setattr(CaseData,'token_data',token_data)
            #提取项目id
        elif case['interface']=='add'and res['msg']:
            loan_id=jsonpath.jsonpath(res,'$..id')[0]
            setattr(CaseData,'loan_id',str(loan_id))

        # 断言
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            if case['check_sql']:
                sql=replace_data(case['check_sql'])
                status=self.db.get_one(sql)[0]
                self.assertEqual(expected['status'],status)
        except AssertionError as e:
            self.excel.write_excel(row=row,column=8,value='未通过')
            mylog.info('用例：{}---->执行未通过'.format(case['title']))
            mylog.error(e)
            print('预期结果：{}'.format(expected))
            print('实际结果：{}'.format(res))
            raise e
        else:
            self.excel.write_excel(row=row,column=8,value='通过')
            mylog.info('用例：{}---->执行已通过'.format(case['title']))

    @classmethod
    def tearDownClass(cls):
        cls.db.close()