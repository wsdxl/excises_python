"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/12 15:17
E-mail  : 506615839@qq.com
File    : test_recharge.py
============================
"""
import unittest
import os
import jsonpath
from common.readexcel import ReadExcel
from common.contants import DATA_DIR
from library.ddt import ddt,data
from common.read_conf import conf
from common.hande_request import HandleRequest
from common.mylogger import mylog
from common.hande_db import Hande_DB
from decimal import Decimal
from common.hande_data import CaseData,replace_data

data_path=os.path.join(DATA_DIR,'cases.xlsx')


@ddt
class TestRecharge(unittest.TestCase):
    excel=ReadExcel(data_path,'recharge')
    case_data=excel.read_excel()
    http=HandleRequest()
    db=Hande_DB()

    @classmethod
    def setUpClass(cls):
        # 准备测试数据
        login_url=conf.get('env','url')+'/member/login'
        data={
            'mobile_phone':conf.get('env','phone'),
            'pwd':conf.get('env','pwd')}
        headers=eval(conf.get('env','headers'))
        # 发送请求
        response=cls.http.send(url=login_url,method='post',json=data,headers=headers)
        res=response.json()
        #保存member_id
        member_id=jsonpath.jsonpath(res,'$..id')[0]
        setattr(CaseData,'member_id',str(member_id))
        token_type=jsonpath.jsonpath(res,'$..token_type')[0]
        token = jsonpath.jsonpath(res, '$..token')[0]
        # 拼接token认证数据
        token_data=token_type+' '+token
        setattr(CaseData,'token_data',token_data)



    @data(*case_data)
    def test_recharge(self,case):
        # 准备测试数据
        recharge_url=conf.get('env','url')+case['url']
        case['data']=replace_data(case['data'])
        recharge_data=eval(case['data'])
        method=case['method']
        headers=eval(conf.get('env','headers'))
        headers['Authorization']=getattr(CaseData,'token_data')
        expected=eval(case['expected'])
        row=case['case_id']+1

        # 发送请求前查询一下账号余额
        if case['check_sql']:
            sql=case['check_sql'].format(conf.get('env','phone'))
            before_amount = self.db.get_one(sql)[0]

        # 发送请求，获取响应结果
        response=self.http.send(url=recharge_url,method=method,json=recharge_data,headers=headers)
        res=response.json()
        #比对预期结果与实际结果
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
            if case['check_sql']:
                sql =case['check_sql'].format(conf.get('env','phone'))
                after_amount=self.db.get_one(sql)[0]
                self.assertEqual((after_amount-before_amount),Decimal(str(recharge_data['amount'])))

        except AssertionError as e:
            self.excel.write_excel(row=row,column=8,value='未通过')
            mylog.info('用例：{}---->测试未通过'.format(case['title']))
            print('预期结果：{}'.format(expected))
            print('实际结果：{}'.format(res))
            mylog.error(e)
            raise e
        else:
            self.excel.write_excel(row=row,column=8,value='已通过')
            mylog.info('用例：{}---->测试已通过'.format(case['title']))


    @classmethod
    def tearDownClass(cls):
        cls.db.close()



if __name__ == '__main__':
    unittest.main()