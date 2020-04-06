"""
============================
Author  : XiaoLei.Du
Time    : 2020/3/13 21:55
E-mail  : 506615839@qq.com
File    : test.py
============================
"""
# print('''hello,python''')
# print(5)
# print(3.141591653)
# import keyword
# print(keyword.kwlist)
# name=input('请输入你的{}'.format('姓名：'))
# print('{},你好！'.format(name))

# import random
# a=random.random()
# print(a)
# b=random.randint(1,9)
# print(b)

# import decimal
# a=4.39
# b=3.85
# a1=decimal.Decimal('4.39')
# b1=decimal.Decimal('3.85')
# print(a-b)
# print(a1-b1)
# print('python'+'java')
# # print(','.join(('python','java')))


# name=input('姓名：')
# sex=input('性别：')
# age=input('年龄：')
#
# print('*'*18+'\n'+'姓名：'+name+'\n'+'性别：'+sex+'\n'+'年龄：'+age+'\n'+'*'*18)

'''
1、用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False（提示:input输入的不管是什么，
都会被转换成字符串，自己扩展，想办法将字符串转换为数值类型，再做判段）
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），
最后计算出应该支付的金额！
3、现在有变量 a = 'hello' ,    b = 'python18'    c = '!' ,
通过相关操作转换成字符串：'hello python18 !'（注意点:转换之后单词之间有空格）

4、使用random模块和字符串拼接的方法，随机生成一个130开头的手机号码。
'''
# print('第一题')
# num = int(input('请输入一个数值：'))
# print(num % 2 == 0)

# print('第二题')
# import random
# price=float(input('请输入橘子的价格：'))
# weight=random.randint(5,10)
# print(weight)
# print('请您支付{:.2f}元'.format(price*weight))

# print('第三题')
# a = 'hello'
# b = 'python18'
# c = '!'
# # d=' '.join((a,b,c))
# # print(d)
#
# print(a+' '+b+' '+c)

# print('第四题')
# from  random import randint
# phone='130'
# for i in range(8):
#     phone+=str(randint(0,9))
# print(phone)

'''
1、现有字符串    str1 = "PHP is the best programming language in the world! "
      要求一：将给定字符串的PHP替换为Python      
      要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表
'''
# str1 ="PHP is the best programming language in the world! "
# str2=str1.replace('PHP','Python')
# print(str2)
# str3=str2.split(' ')
# print(str3)

'''
2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”（要求：使用上课学过的知识点来做） 
'''
# l=['一','二','三','四','五','六','日']
# num=int(input('请输入1-7的数字:'))
# print('今天是周{}'.format(l[num-1]))


'''
3、现在有一个列表 li2=[1，2，3，4，5]，

     第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，

     第二步：对li2进行升序排序 （从小到大）

     第三步：对第二步排序后的列表  再进行降序排序（从大到小）
'''
# li2=[1,2,3,4,5]
# li2.insert(0,0)
# print(li2)
# li2[4]=66
# print(li2)
# li2.extend([11,22,33])
# print(li2)
# li2.sort()
# print(li2)
# li2.reverse()
# print(li2)


'''
 4、切片 

        1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9] 

        2、s = 'python java php',通过切片获取: java
'''
# li = [1,2,3,4,5,6,7,8,9]
# li1=li[2::3]
# print(li1)

# s = 'python java php'
# s1=s[7:11]
# print(s1)

'''
# 5、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，
# 将输入的信息添加的列表中保存，然后按照一下格式输出：
#     用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对（要求：输出的身高要求保留2位小数）
# '''
# user=[]
# name=input('请输入姓名：')
# age= int(input('请输入年龄：'))
# height=float(input('请输入身高：'))
# user.append(name)
# user.append(age)
# user.append(height)
# print('用户的姓名为：{},年龄为：{},身高为：{:.2f},请仔细核对'.format(name,age,height))


# # find :查找字符串片段在字符串中的下标位置，如果没有返回-1
# s1='abcd234abcd'
# res=s1.find('d',4)
# print(res)
# res1=s1.find('e')
# print(res1)
# # count:统计字符串片段出现的次数，如果没有就返回0
# res2=s1.count('b')
# res3=s1.count('e')
# print(res2,res3)
#
# # replace：替换字符串片段
# res4=s1.replace('abcd','ABCD',2)
# print(res4)

# s3='111ab222ab333AB444'
# res5=s3.split('a',1)
# print(res5)
# res6=s3.upper()
# print(res6)
#
# res7=s3.lower()
# print(res7)


# str1='今收到{0},交了学费{0}元，开此收据为凭据'
# print(str1.format('jack',500))

# price=float(input('请输入价格：'))
# print('今天xx股票的价格是{:.2f}元'.format(price))
#
# print('百分比是{:.2%}'.format(0.25))

# print('{:<8}*****'.format('abc'))
# # print('{:>8}*****'.format('abc'))
# # print('{:^8}*****'.format('abc'))

# print('我的名字叫%s,我今年%d岁了，我是一个%s孩子！'%('小明',19,'男'))
#
# name='小明'
# age=19
# sex='男'
# print(f'我的名字叫{name},我今年{age}岁了，我是一个{sex}孩子！')

# list=[2,5,6,8,3,22,67,12]
# list.insert(0,1)
# print(list)
#
# list[6]=33
# print(list)
# list.extend(['aa','bb','cc'])
# print(list)
# list.append('dd')
# print(list)

# li3=[1,2,3,11,22,33,1,2,3]
# li3.remove(11)
# print(li3)
# li3.pop(3)
# print(li3)


# li5=[111,22,31,41,5,6,888,8,34,8,12,7,33]
# li6=li5
# li7=li5.copy()
#
# print(id(li5))
# print(id(li6))
# print(id(li7))


# li4=['aa','bb',11,22,33]
# print('aa' in li4)
# print('cc' in li4)

# li = [11, 22, 33]
# li2 = [11, 22, 33]
# print(id(li))
# print(id(li2))


# dic2={'aa':11,'bb':22,'cc':22}
# dic2['dd']=33
# print(dic2)
#
# dic2.update({'a':1,'b':2})
# print(dic2)

# a='2frrgtfddgfv'
# b=a[1:3]
# print(b)

# dic4={'aa':11,'bb':22,'cc':22,'dd':999,'a':1,'b':2,'c':3}
# print(list(dic4.keys()))
# print(list(dic4.values()))
# print(list(dic4.items()))

# dic5=dict(name='小明',age=18,sex='男')
# print(dic5)
#
# dic6=dict([('aa',11),('bb',22),('cc',33)])
# print(dic6)
#
# s={1,2,'aa',(2,4)}
# print(s)

'''
一、请指出下面那些为可变类型的数据，那些为不可变类型的数据

1、 (11) ,数值，不可变量   
2、 {11，22}，集合，可变量
3、 ([11,22,33])，列表，可变量
4、 {"aa":111}，字典，可变量
'''
'''
二、有5道题（通过字典来存储数据）： 某比赛需要获取你的个人信息，设计一个程序， 
 1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
 3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 
 4、平台为了保护你的隐私，需要你删除你的联系方式；
 5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
'''
# name=input('请输入姓名：')
# sex=input('请输入性别：')
# age=input('请输入年龄：')
# info={'姓名':name,'性别':sex,'年龄':age}
# print('我的名字{},今年{}岁,性别{},喜欢敲代码'.format(name,age,sex))
# info.update({'height':170,'phone':13888888888})
# print(info)
# info.pop('phone')
# print(info)
# info['skill']='爱劳动'
# print(info)

'''
三、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
 要求一：去除列表中的重复元素，
 要求二：删除 77，88，99这三个元素
'''
# li = [11,22,33,22,22,44,55,77,88,99,11]
# li1=list(set(li))
# print(li1)
# li1.sort()
# print(li1)
# # li2=li1[:5]
# # print(li2)
# li1.pop()
# li1.pop()
# li1.pop()
# print(li1)

'''
四、有下面几个数据 ，
t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]
请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":22,"bb":22}
要注意字典中元素的位置（使用python3.5以下的同学不用考虑位置）
'''
# t1 = ("aa",11)
# t2= ("bb",22)
# li1 = [("cc",11)]
#
# # dic=dict([t1,li1[0],t2])
# # print(dic)
# # dic['cc']=22
# # print(dic)
# li1.append(t2)
# li1.insert(0,t1)
# dic=dict(li1)
# dic['cc']=22
# print(dic)

# 考试成绩等级区分

"""
40 > x            E
40<= x <60        D 
60<= x <75        C
75<= x <85        B
85<= x <=100      A

"""
# score=float(input('请输入成绩：'))
# if 0<= score <40:
#     print('您的评级为E')
# elif 40<=score <60:
#     print('您的评级为D')
# elif 60<=score <75:
#     print('您的评级为C')
# elif 75<=score <85:
#     print('您的评级为B')
# elif 85<=score <100:
#     print('您的评级为A')
# else:
#     print('您的输入不合法')

'''
需求：打印100遍hello python,
需求：第50遍打印两遍
'''
# num=1
# while num<=100:
#     print('hello python',num)
#     if num==50:
#         print('hello python', num)
#     num+=1

# 计算 1+2+3+....100
# s=0
# n=1
#
# while n<=100:
#     s+=n
#     n+=1
#     if n==50:
#         break
#     print(n, s)
# else:
#     print('结束吧')
# print(s)

# dic = {"aa": 11, "bb": 22, "cc": 33}
# #
# # # for i in dic:
# # #     print(i)
# #
# # for i,v in dic.items():
# #     print(i,v)

# t = (111, 222)
# a,b=t
# print(a,b)
# m,n=111,222
# print(m,n)

# 2、一个 5 位数，判断它个位与万位相同，十位与千位相
# 同。 根据判断打印出相关信息。
# num=(input('请输入一个五位数：'))
# if num[-1]==num[0] and num[-2]==num[1]:
#     print('此数值符合规范')
# else:
#     print('此数值符合规范')

#  3、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，
#  则 印大于随机数。小了，则打印小于随机数。如果相等，则打印等于随机数

# import random
# a=random.randint(1,9)
# num =int(input('请输入一个数字：'))
# if num>a:
#     print('num的值是{},a的值是{},大于随机数'.format(num,a))
# elif num<a:
#     print('num的值是{},a的值是{},小于随机数'.format(num, a))
# elif num==a:
#     print('num的值是{},a的值是{},等于随机数'.format(num, a))
# else:
#     print('你的输入有误')

'''
4、实现剪刀石头布游戏（），提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4） 
电脑随机出拳比较胜负，显示 用户胜、负还是平局。

胜利 
user 1,com 2  -1
user 2,com 3  -1
user 3,com 1  2
输
user 1,com 3  -2
user 2,com 1  1
user 3,com 2  1


'''
from random import randint

# print('*'*4+'石头剪刀布游戏开始'+'*'*4)
# print('请按下面的提示出拳：')
# list=['石头','剪刀','布']

# while True:
#     print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
#     com=randint(1,3)
#     user=int(input('请输入你的选项：'))
#     if 1<=user<=3:
#         if (user-com==-1) or (user-com==2):
#             print('你的出拳为:{},电脑出拳:{},你胜利了'.format(list[user-1],com))
#         elif (user-com==-2) or (user-com==1):
#             print('你的出拳为:{},电脑出拳:{},你输了'.format(list[user - 1], com))
#         elif user ==com:
#             print('你的出拳为:{},电脑出拳:{},平局'.format(list[user - 1], com))
#
#     elif user==4:
#         print('结束游戏')
#         break
#     else:
#         print('你的输入有误，请按规则出拳')

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={:<4}'.format(i,j,(i*j)),end=' ')
#     print('')

'''
2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
'''
# num=0
# for i in range(1,5):
#     for j in range(1,5):
#         for v in range(1,5):
#             if i !=j and j !=v and v !=i:
#                 num+=1
#                 print(num,str(i)+str(j)+str(v))

# def func():
#     for i in range(1, 6):
#         for j in range(1, i + 1):
#             print(j, end=' ')
#         print('')
# func()


# s1 = 'a1a1a'
# # res = s1.split('1')
# # print(res)

# # li = [11, 22, 33]
# # res2 = li.append(11)
# # print(res2)
# def func(a,b):
#     print('a',a)
#     print('b',b)
# dic={'a':11,'b':22}
# func(**dic)

'''
3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ：   
加【1】    减【2】    乘【3】      除【4】，根据不同的选择完成不同的计算 
每个方法使用一个函数来实现， 选择后调用对应的函数，然后返回结果。
'''

# def jia(a, b):
#     '''加法'''
#     return (a + b)
#
#
# def jian(a, b):
#     '''减法'''
#     return (a - b)
#
#
# def cheng(a, b):
#     '''乘法'''
#     return (a * b)
#
#
# def chu(a, b):
#     '''除法'''
#     return (a / b)
#
#
# def counter():
#     n1 = int(input('请输入数字1：'))
#     n2 = int(input('请输入数字2：'))
#     com = input('请选择加【1】减【2】乘【3】除【4】：')
#     if com == '1':
#         return jia(n1, n2)
#     elif com == '2':
#         return jian(n1, n2)
#     elif com == '3':
#         return cheng(n1, n2)
#
#     elif com == '4':
#         return chu(n1, n2)
#
# s=counter()
# print(s)

'''
4、学习控制流程时，我们讲了一个登录的案例，现在要求大家通过代码实现一个注册的流程
1、运行程序，提示用户，输入用户名，输入密码，再次确认密码。
2、判读用户名有没有被注册过，如果用户名被注册过了，那么打印结果该用户名已经被注册。
3、用户名没有被注册过，则判断两次输入的密码是否一致，一致的话则注册成功，否则给出对应的提示。
'''
# def register():
#     while True:
#         users=[{'user':'test1','pass':123}]
#         username=input('请输入用户名：')
#         for i in users:
#             if username==i['user']:
#                 print('该用户名已经注册')
#                 break
#         else:
#             passname1 = input('请输入密码：')
#             passname2 = input('请再次输入密码：')
#             if passname1 !=passname2:
#                 print('两次密码不一致')
#             else:
#                 users.append({'user':username,'pass':passname2})
#                 print('注册成功')
#                 print(users)
#                 break
#
# register()


'''
现在有以下数据， li1 = ["{'a':11,'b':2}","[11,22,33,44]"] 
需要转换为以下格式： li1 = [{'a':11,'b':2},[11,22,33,44]] 
'''
# li1 = ["{'a':11,'b':2}","[11,22,33,44]"]
# def work():
#     li2=[]
#     for i in li1:
#         li2.append((eval(i)))
#     return li2
# res=work()
# print(res)

'''
# 有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
# 要求一：把上述数据转换为以下格式
res1 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
# 要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
res = [
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
'''
#
# cases = [
#     ['case_id', 'case_title', 'url', 'data', 'excepted'],
#     [1, '用例1', 'www.baudi.com', '001', 'ok'],
#     [4, '用例4', 'www.baudi.com', '002', 'ok'],
#     [2, '用例2', 'www.baudi.com', '002', 'ok'],
#     [3, '用例3', 'www.baudi.com', '002', 'ok'],
#     [5, '用例5', 'www.baudi.com', '002', 'ok'],
# ]
#
# def work1(datas):
#     datas = []
#     for item in cases[1:]:
#         # print(item)
#         data = dict(zip(cases[0], item))
#         datas.append(data)
#     return (datas)
#
# def work2(datas):
#     datas1 = []
#     for a in datas:
#         if a['case_id'] > 3:
#             datas1.append(a)
#     return (datas1)
#
# res1=work1(cases)
# print(res1)
# res2=work2(res1)
# print(res2)

# li1 = [11, 22, 33, 44, 55, 66]
# s = "sfsdgfsk"
# li2=enumerate(li1)
# print(list(li2))

# 要求：请将数据读取出来，转换为以下格式
# {'data0': '数据aaa', 'data1': '数据bbb', 'data2': '数据ccc', 'data3': '数据ddd'}

# def work3():
#     with open(file='datas.txt',mode='r',encoding='utf8') as f:
#         datas=f.readlines()
#         # print(datas)
#         dic={}
#         for i,v in  enumerate(datas):
#             # print(i,v)
#             key='data{}'.format(i)
#             value=v.strip()
#             dic[key]=value
#         return (dic)
# data=work3()
# print(data)

'''
# 要求一： 请把这些数据读取出来，到并且存到list中，格式如下
[
{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
]
# 要求二：将上述数据再次进行转换，转换为下面这种字典格式格式
​
{
   'data1':{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, 
   'data2':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}, 
   'data3':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},   
   'data4':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
   'data5':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
}
'''
# def work5():
#     with open(file='case.txt',mode='r',encoding='utf8') as f:
#         datas=f.readlines()
#         # print(datas)
#         data1=[]
#         for i in datas:
#             data=i.strip().split(',')
#             # print(data)
#             dic={}
#             for v in data:
#                 key=v.split(':')[0]
#                 value=v.split(':')[1]
#                 dic[key]=value
#             data1.append(dic)
#         return (data1)
# #
# data=work5()
# print(data)
#
# def work6(data):
#     dic1={}
#     for i,v in  enumerate(data):
#         # print(i,v)
#         key='data{}'.format(i+1)
#         value=v
#         dic1[key]=value
#     return (dic1)
#
# datas1=work6(data)
# print(datas1)

# with open(file='data.txt',mode='r',encoding='utf8') as f:
#     users=eval(f.read())
#     # print(users)
#     while True:
#         # users=[{'user':'test1','pass':123}]
#         username=input('请输入用户名：')
#         for i in users:
#             if username==i['user']:
#                 print('该用户名已经注册')
#                 break
#         else:
#             passname1 = input('请输入密码：')
#             passname2 = input('请再次输入密码：')
#             if passname1 !=passname2:
#                 print('两次密码不一致')
#             else:
#                 users.append({'user':username,'pass':passname2})
#                 print('注册成功')
#                 print(users)
#                 break
#
# with open(file='data.txt',mode='w',encoding='utf8') as f:
#     f.write(str(users))

# import os
#
# print(__file__)
# dir=os.path.dirname(__file__)
# print(dir)
# basedir=os.path.dirname(os.path.dirname(__file__))
# print(basedir)
# file_path=os.path.join(basedir,'interface_test/test.py')
# print(file_path)
#
# if __name__ == "__main__":
#     pass

# try:
#     with open(file='data.txt',mode='r',encoding='utf8') as f:
#         users=eval(f.read())
# except:
#     users=[]
#         # print(users)
# while True:
#     # users=[{'user':'test1','pass':123}]
#     username=input('请输入用户名：')
#     for i in users:
#         if username==i['user']:
#             print('该用户名已经注册')
#             break
#     else:
#         passname1 = input('请输入密码：')
#         passname2 = input('请再次输入密码：')
#         if passname1 !=passname2:
#             print('两次密码不一致')
#         else:
#             users.append({'user':username,'pass':passname2})
#             print('注册成功')
#             print(users)
#             break
#
# with open(file='data.txt',mode='w',encoding='utf8') as f:
#     f.write(str(users))

# from random import randint
#
# print('*'*4+'石头剪刀布游戏开始'+'*'*4)
# print('请按下面的提示出拳：')
# list=['石头','剪刀','布']
#
# while True:
#     print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
#     com=randint(1,3)
#     try:
#         user=int(input('请输入你的选项：'))
#     except:
#         print('你的输入有误，请按规则出拳')
#     else:
#         if 1 <= user <= 3:
#             if (user - com == -1) or (user - com == 2):
#                 print('你的出拳为:{},电脑出拳:{},你胜利了'.format(list[user - 1], com))
#             elif (user - com == -2) or (user - com == 1):
#                 print('你的出拳为:{},电脑出拳:{},你输了'.format(list[user - 1], com))
#             elif user == com:
#                 print('你的出拳为:{},电脑出拳:{},平局'.format(list[user - 1], com))
#
#         elif user == 4:
#             print('结束游戏')
#             break
#         else:
#             print('你的输入有误，请按规则出拳')

'''
4、封装一个学生类，(自行分辨定义为类属性还是实例属性)
-  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
-  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息。
'''
# class Student:
#     identity='学生'
#
#     def __init__(self,name,age,sex,english,math,chinese):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.english=english
#         self.math=math
#         self.chinese=chinese
#
#     def sum_score(self):
#         return self.english+self.math+self.chinese
#
#     def avg_score(self):
#         return (self.english+self.math+self.chinese)/3
#
#     def info(self):
#         print('姓名:{},年龄:{},性别:{}'.format(self.name,self.age,self.sex))
#
# student=Student('小明',20,'男',88,95,98)
# print(student.sum_score())
# print(student.avg_score())
# student.info()

'''
5、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，
-  属性：用例编号  url地址   请求参数   请求方法    预期结果   实际结果
'''
# class TestCase:
#     def __init__(self,case_id,url,data,method,expected,result):
#         self.case_id=case_id
#         self.url=url
#         self.data=data
#         self.method=method
#         self.expected=expected
#         self.result=result
# import random
# class MyClass:
#     attr=100
#     __attr=200
#
#     def func(self):
#         '''调用静态方法'''
#         a=self.__attr
#         print(a)
#         phone=self.random_phone()
#         print('这是一个实例方法')
#
#     @classmethod
#     def cls_func(cls):
#         b=cls.__attr
#         print(b)
#         print('这是一个类方法')
#
#     @staticmethod
#     def static_func():
#         print('这是一个静态方法')
#
#     @staticmethod
#     def random_phone():
#         phone='13'
#         for i in range(9):
#             phone+=str(random.randint(0,9))
#         return phone
#
#
# myclass=MyClass()
# myclass.func()
# myclass.cls_func()
# phone=myclass.random_phone()
# print(phone)
# print(myclass.attr)
# # print(myclass.__attr)

# class BasePhone():
#     def call_phone(self):
#         print('拨打语音电话')
#
# class PhoneV1(BasePhone):
#     def dis_play(self):
#         print('播放音乐')
#
#     def send_msg(self):
#         print('发送信息')
#
# class PhoneV2(PhoneV1):
#
#     def call_phone(self):
#         '''重新父类方法'''
#         print('拨打视频电话')
#         # super().call_phone()
#         BasePhone.call_phone(self)
#
#     def game(self):
#         print('打游戏')
#
#
# phone=PhoneV2()
# phone.game()
# phone.dis_play()
# phone.send_msg()
# phone.call_phone()

cases = [
    {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'},
    {'case_id': 2, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '通过', 'excepted': '通过'},
    {'case_id': 3, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'},
    {'case_id': 4, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '通过', 'excepted': '通过'},
    {'case_id': 5, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'},
    {'case_id': 6, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '通过', 'excepted': '通过'},
]


class CaseData:
    pass


li = []
for item in cases:
    case = CaseData()
    for i, v in item.items():
        setattr(case, i, v)
    li.append(case)
print(li)
