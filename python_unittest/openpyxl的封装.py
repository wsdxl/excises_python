"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/6 21:06
E-mail  : 506615839@qq.com
File    : openpyxl的封装.py
============================
"""
import openpyxl
class CaseData:
    pass

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
        rows = list(self.sh.rows)
        list_data=[]
        title=[]
        for i in rows[0]:
            title.append(i.value)

        for v in rows[1:]:
            data=[]
            for row in v:
                data.append(row.value)
            datas=dict(zip(title,data))
            list_data.append(datas)
        return (list_data)

    def read_excel_object(self):
        # 1、打开工作簿，选中表单
        self.open()
        rows = list(self.sh.rows)
        list_data = []
        title = []
        for i in rows[0]:
            title.append(i.value)
        class MyDada:
            pass

        for v in rows[1:]:
            data = []
            for row in v:
                data.append(row.value)
            datas = list(zip(title, data))
            cases = CaseData()
            for m,n in datas:
                setattr(cases,m,n)
            list_data.append(cases)
        return (list_data)





    def write_excel(self,row,column,value):
        self.open()
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.filename)






if __name__ == '__main__':
    excel = ReadExcel('cases.xlsx', 'register')
    excel.read_excel_object()
