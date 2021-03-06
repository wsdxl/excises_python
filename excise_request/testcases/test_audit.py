"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/15 10:42
E-mail  : 506615839@qq.com
file:   test_audit.py
============================
"""
import unittest
import os
import jsonpath
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.contants import DATA_DIR
from common.read_conf import conf
from common.hande_request import HandleRequest
from common.hande_data import CaseData, replace_data
from common.mylogger import mylog
from common.hande_db import Hande_DB

file_path = os.path.join(DATA_DIR, 'cases.xlsx')


@ddt
class TestAudit(unittest.TestCase):
    excel = ReadExcel(file_path, 'audit')
    audit_data = excel.read_excel()
    http = HandleRequest()
    db=Hande_DB()

    @classmethod
    def setUpClass(cls):
        url = conf.get('env', 'url') + '/member/login'
        data = {"mobile_phone": conf.get('env', 'admin_phone'),
                "pwd": conf.get('env', 'admin_pwd')
        }
        headers = eval(conf.get('env', 'headers'))
        response = cls.http.send(url=url, method='post', json=data, headers=headers)
        res = response.json()

        # 提取token值和member_id
        id = jsonpath.jsonpath(res, '$..id')[0]
        setattr(CaseData, 'member_id', str(id))
        token_type = jsonpath.jsonpath(res, '$..token_type')[0]
        token = jsonpath.jsonpath(res, '$..token')[0]
        token_data = token_type +' ' + token
        setattr(CaseData, 'token_data', token_data)

    def setUp(self):
        url = conf.get('env', 'url') + '/loan/add'
        data= {
            "member_id":getattr(CaseData,'member_id'),
            "title":"升职加薪",
            "amount":5000,
            "loan_rate":18,
            "loan_term":12,
            "loan_date_type":1,
            "bidding_days":6
        }
        headers=eval(conf.get('env','headers'))
        headers['Authorization']=getattr(CaseData,'token_data')

        response=self.http.send(url=url,method='post',json=data,headers=headers)
        res=response.json()
        # 提取id
        loan_id=jsonpath.jsonpath(res,'$..id')[0]
        setattr(CaseData,'loan_id',str(loan_id))



    @data(*audit_data)
    def test_audit(self,case):
        # 准备测试数据
        # 准备url地址
        url=conf.get('env','url')+case['url']
        # 请求方法
        method=case['method']
        # 请求数据
        case['data']=replace_data(case['data'])
        data=eval(case['data'])
        print('data:',data)
        #配置文件获取headers
        headers=eval(conf.get('env','headers'))
        headers['Authorization']=getattr(CaseData,'token_data')

        # 预期结果
        expected=eval(case['expected'])

        row=case['case_id']+1
        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()
        print('audit_res:',res)

        if case['title']=='审核通过' and res['msg']=='OK':
            pass_loan_id=getattr(CaseData,'loan_id')
            setattr(CaseData,'pass_loan_id',pass_loan_id)

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
            print("预期结果：{}".format(expected))
            print("实际结果：{}".format(res))
            raise e
        else:
            self.excel.write_excel(row=row,column=8,value='已通过')
            mylog.info('用例：{}---->执行已通过'.format(case['title']))


if __name__ == '__main__':
    unittest.main()