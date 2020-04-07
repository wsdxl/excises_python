"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/6 21:44
E-mail  : 506615839@qq.com
File    : readexcel.py
============================
"""

import openpyxl

# 用来创建对象保存用例数据的类
class CaseData:
    pass

# 创建读取测试数据类
class ReadExcel(object):

    def __init__(self, filename, sheetname):
        '''
        初始化方法
        :param filename: excel文件名
        :param sheetname: 表单名
        '''
        self.filename = filename
        self.sheetname = sheetname

    def open(self):
        '''打开工作簿，选中表单'''
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheetname]

    def close(self):
        '''关闭工作簿，释放资源'''
        self.wb.close()

    def read_excel(self):
        '''

        :return: 列表嵌套字典格式
        '''
        # 1、打开工作簿，选中表单
        self.open()
        # 以列表格式读取所有表格
        rows = list(self.sh.rows)
        list_data = []
        title = []
        # 遍历表头，存放入列表
        for i in rows[0]:
            title.append(i.value)
        # 遍历除了表头外的其他表格
        for v in rows[1:]:
            data = []
            for row in v:
                data.append(row.value)
            datas = dict(zip(title, data))
            list_data.append(datas)
        self.close()
        return (list_data)

    def read_excel_object(self):
        # 1、打开工作簿，选中表单
        self.open()
        rows = list(self.sh.rows)
        list_data = []
        title = []
        for i in rows[0]:
            title.append(i.value)

        for v in rows[1:]:
            data = []
            for row in v:
                data.append(row.value)
            datas = list(zip(title, data))
            cases = CaseData()
            for m, n in datas:
                setattr(cases, m, n)
            list_data.append(cases)
        self.close()
        return (list_data)


    def write_excel(self,row,column,value):
        '''

        :param row: 行
        :param column: 宽
        :param value: 值
        :return:
        '''
        self.open()
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.filename)
        self.close()
