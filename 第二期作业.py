#!/usr/bin/env python
# _*_ coding:  utf-8  _*_
#@Time  :  2020/1/8 
#@Author:  Leo

'''
1.
age = int(input("用户输入年龄："))
if str(age).isdigit():                            #.isdigit() 前面要用str长转
    if age >= 18:
        print("恭喜你，成年了！")
    else:
        print("你好，小朋友")

else:
    print("您的输入有误!")
'''

'''
2.

'''
name = input('输入您的姓名：')
age = int(input('输入您的年龄'))
phone  = int(input('输入您的电话号码：'))
y_n = input('你是否选择打印：')
if y_n.upper() == 'Y':
    print("欢迎来到logic，请确认信息，您的姓名是{}，年龄为{},电话是{}".format(name,age,phone))
elif y_n.upper() == 'N':
    print("很高心为您服务")
else:
    print("您的输入有误")

