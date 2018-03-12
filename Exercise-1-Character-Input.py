#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Exercise
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''


import datetime

while True:
    name = input("请输入您的名字：")
    age = int(input("请输入您的年龄："))

    now = datetime.datetime.now()

    this_year = now.year

    print(name + "在" + str(this_year - age + 100) + "年的年龄是100岁")
    print()
    in_program = input("请问您需要继续吗？输入任意键继续，输入0结束程序：")

    if in_program == '0':
        break
