"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/12 20:25
E-mail  : 506615839@qq.com
File    : hande_db.py
============================
"""
import pymysql
from common.read_conf import conf
class Hande_DB:
    def __init__(self):
        self.con=pymysql.connect(host=conf.get('mysql','host'),
                                user=conf.get('mysql','user'),
                                password=conf.get('mysql','password'),
                                port=conf.getint('mysql','port'),
                                charset='utf8'
                                )
        self.cur=self.con.cursor()

    def get_one(self,sql):
        '''获取查询到的第一条数据'''
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self,sql):
        '''获取查询到的所有数据'''
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def count(self,sql):
        '''获取查询到的数据条数'''
        self.con.commit()
        res=self.cur.execute(sql)
        return res

    def close(self):
        # 关闭游标对象
        self.cur.close()
        # 断开连接
        self.con.close()

if __name__ == '__main__':
    db=Hande_DB()
    sql='select * from futureloan.loan where member_id="{}"'.format(8029418)
    count=db.count(sql)
    print(count,type(count))

