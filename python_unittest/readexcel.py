"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/6 21:44
E-mail  : 506615839@qq.com
File    : readexcel.py
============================
"""

import openpyxl


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

    def save(self):
        self.wb.save(self.filename)

    def read_excel(self):
        # 1、打开工作簿，选中表单
        self.open()
        max_row = self.sh.max_row
        list_data=[]
        for i in range(1, max_row + 1):
            data1 = self.sh.cell(row=i, column=1).value
            data2 = self.sh.cell(row=i, column=2).value
            data3 = self.sh.cell(row=i, column=3).value
            data4 = self.sh.cell(row=i, column=4).value
            list_data.append([data1,data2,data3,data4])
        # print(list_data)
        title=list_data[0]
        cases=[]
        for i in list_data[1:]:
            data=dict(zip(title,i))
            cases.append(data)
        return (cases)



    def write_excel(self):
        pass
