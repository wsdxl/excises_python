"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/11 22:16
E-mail  : 506615839@qq.com
File    : test_login.py
============================
"""
import os
import unittest
from library.ddt import ddt,data
from common.readexcel import ReadExcel
from common.contants import DATA_DIR
from common.read_conf import conf
from common.hande_request import HandleRequest
from common.mylogger import mylog


case_path=os.path.join(DATA_DIR,'cases.xlsx')

@ddt
class TestLogin(unittest.TestCase):
    excel=ReadExcel(case_path,'login')
    case_data=excel.read_excel()
    http=HandleRequest()

    @data(*case_data)
    def test_login(self,case):
        # 准备测试数据
        url=conf.get('env','url')+case['url']
        method=case['method']
        if '#phone#' in case['data']:
            case['data']=case['data'].replace('#phone#',conf.get('env','phone'))
        data=eval(case['data'])
        expected=eval(case['expected'])
        headers=eval(conf.get('env','headers'))
        row=case['case_id']+1
        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()
        # 比对预期结果与实际结果
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'], res['msg'])
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