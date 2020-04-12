"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/12 18:35
E-mail  : 506615839@qq.com
File    : 数据库操作.py
============================
"""
import pymysql
'''
python操作mysql需要使用pymysql这个模块，

主机：120.78.128.25
port：3306
用户：future
密码：123456
'''
# 第一步：连接mysql数据库
con=pymysql.connect(host='120.78.128.25',
                    user='future',
                    password='123456',
                    port=3306,
                    charset='utf8'
)
# 第二步：创建一个游标对象
cur=con.cursor()

# 第三步：执行sql语句
# 1.准备sql语句
sql='select * from futureloan.member order by id desc limit 5;'
# 2.执行sql语句
res=cur.execute(sql)
# print(res)
# 第四步：提出要查找的内容
datas=cur.fetchall()
for i in datas:
    print(i)
# data=cur.fetchone()
# print(data[3])
