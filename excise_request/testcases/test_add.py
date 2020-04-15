"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/15 0:09
E-mail  : 506615839@qq.com
File    : test_add.py
============================
"""
import unittest
import os
import jsonpath
from  library.ddt import ddt,data
from common.readexcel import ReadExcel
from common.contants import DATA_DIR
from common.read_conf import conf
from common.hande_data import CaseData,replace_data
from common.hande_request import HandleRequest
from common.hande_db import Hande_DB
from common.mylogger import mylog

file_path=os.path.join(DATA_DIR,'cases.xlsx')

@ddt
class TestAdd(unittest.TestCase):
    excel=ReadExcel(file_path,'add')
    cases=excel.read_excel()
    http=HandleRequest()
    db=Hande_DB()


    @data(*cases)
    def test_add(self,case):
        # 准备测试数据
        url=conf.get('env','url')+case['url']
        case['data']=replace_data(case['data'])
        data=eval(case['data'])
        headers=eval(conf.get('env','headers'))
        if case['interface'] !='登录':
            headers['Authorization']=getattr(CaseData,'token_data')
        method=case['method']
        expected=eval(case['expected'])
        row=case['case_id']+1

        # 请求前查看该用户有几条标记录
        if case['check_sql']:
            sql=case['check_sql'].format(getattr(CaseData,'admin_member_id'))
            before_count=self.db.count(sql)



        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()
        # 如果是登录接口，提取出id和token值
        if case['interface']=='登录':
            id=jsonpath.jsonpath(res,'$..id')[0]
            setattr(CaseData,'admin_member_id',str(id))
            token_type=jsonpath.jsonpath(res,'$..token_type')[0]
            token = jsonpath.jsonpath(res, '$..token')[0]
            token_data=token_type+' '+token
            setattr(CaseData,'token_data',token_data)


        # 断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])

            if case['check_sql']:
                sql =case['check_sql'].format(getattr(CaseData,'admin_member_id'))
                after_count = self.db.count(sql)
                self.assertEqual((after_count-before_count),1)


        except AssertionError as e:
            self.excel.write_excel(row=row, column=8, value='未通过')
            mylog.info('用例：{}---->测试未通过'.format(case['title']))
            print('预期结果：{}'.format(expected))
            print('实际结果：{}'.format(res))
            mylog.error(e)
            raise e
        else:
            self.excel.write_excel(row=row, column=8, value='已通过')
            mylog.info('用例：{}---->测试已通过'.format(case['title']))


    @classmethod
    def tearDownClass(cls):
        cls.db.close()