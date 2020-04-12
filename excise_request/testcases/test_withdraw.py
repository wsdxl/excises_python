"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/12 18:06
E-mail  : 506615839@qq.com
File    : test_withdraw.py
============================
"""
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
from library.ddt import ddt, data
from common.read_conf import conf
from common.hande_request import HandleRequest
from common.mylogger import mylog
from common.hande_db import Hande_DB
from decimal import Decimal

data_path = os.path.join(DATA_DIR, 'cases.xlsx')


@ddt
class TestWithdraw(unittest.TestCase):
    excel = ReadExcel(data_path, 'withdraw')
    case_data = excel.read_excel()
    http = HandleRequest()
    db=Hande_DB()

    @data(*case_data)
    def test_withdraw(self, case):
        # 准备测试数据
        withdraw_url = conf.get('env', 'url') + case['url']
        if '#member_id#' in case['data']:
            case['data'] = case['data'].replace('#member_id#', str(self.member_id))
        if '#phone#' in case['data']:
            case['data'] = case['data'].replace('#phone#', conf.get('env', 'phone'))
        withdraw_data = eval(case['data'])
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        if case['interface'] !='登录':
            headers['Authorization'] =self.token_data
        expected = eval(case['expected'])
        row = case['case_id'] + 1

        # 发送请求前查询账号余额
        if case['interface'] !='登录':
            sql = 'select * from futureloan.member where mobile_phone={}'.format(conf.get('env', 'phone'))
            before_amount = self.db.get_one(sql)[5]

        # 发送请求，获取响应结果
        response = self.http.send(url=withdraw_url, method=method, json=withdraw_data, headers=headers)
        res = response.json()

        # 判断是登录接口还是提现接口
        if case['interface'] == '登录':
            TestWithdraw.member_id = jsonpath.jsonpath(res, '$..id')[0]
            token_type = jsonpath.jsonpath(res, '$..token_type')[0]
            token = jsonpath.jsonpath(res, '$..token')[0]
            TestWithdraw.token_data = token_type + ' ' + token

        # 比对预期结果与实际结果
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])

            if case['interface']!='登录' and res['msg']=='OK':
                sql = 'select * from futureloan.member where mobile_phone={}'.format(conf.get('env', 'phone'))
                after_amount = self.db.get_one(sql)[5]
                self.assertEqual((before_amount-after_amount),Decimal(str(withdraw_data['amount'])))


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


if __name__ == '__main__':
    unittest.main()