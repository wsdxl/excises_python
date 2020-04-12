"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/11 16:22
E-mail  : 506615839@qq.com
File    : test_register.py
============================
"""
import os
import random
import unittest
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.contants import DATA_DIR
from common.hande_request import HandleRequest
from common.read_conf import conf
from common.mylogger import mylog
from common.hande_db import Hande_DB

case_path = os.path.join(DATA_DIR, 'cases.xlsx')


@ddt
class TestRegister(unittest.TestCase):
    excel = ReadExcel(case_path, 'register')
    case_data = excel.read_excel()
    http = HandleRequest()
    db=Hande_DB()

    @data(*case_data)
    def test_register(self, case):
        # 准备测试数据
        # 拼接完整的接口地址
        url = conf.get('env', 'url') + '/member/register'
        # 请求方法
        method = case['method']
        if '#phone#' in case['data']:
            phone = self.random_phone()
            case['data'] = case['data'].replace('#phone#', phone)
        data = eval(case['data'])

        expected = eval(case['expected'])
        headers = eval(conf.get('env', 'headers'))
        row = case['case_id'] + 1
        # 2、发送请求
        response = self.http.send(url=url, method=method, json=data, headers=headers)
        res = response.json()

        # 3、比对预期结果与实际结果
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            if res['msg']=='OK':
                sql='select * from futureloan.member where mobile_phone={}'.format(phone)
                count=self.db.count(sql)
                self.assertEqual(count,1)
        except AssertionError as e:
            self.excel.write_excel(row=row, column=8, value='未通过')
            mylog.info('用例：{}----->执行未通过'.format(case['title']))
            mylog.error(e)
            print("预期结果：{}".format(expected))
            print("实际结果：{}".format(res))
            raise e
        else:
            self.excel.write_excel(row=row, column=8, value='已通过')
            mylog.info('用例：{}----->执行已通过'.format(case['title']))

    @staticmethod
    def random_phone():
        phone = '13'
        for i in range(9):
            phone += str(random.randint(0, 9))
        return phone

    @classmethod
    def tearDownClass(cls) :
        cls.db.close()


if __name__ == '__main__':
    unittest.main()
