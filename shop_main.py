#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pymysql
import re
from user_login_reg import *

def shop_main():
    '''
    函数功能:小型超市商品信息管理系统, 需要登录后才能使用, 超市老板和员工可以使用同一界面
    登录进行操作, 但超市老板具有管理员权限, 管理员默认用户名为'Root123', 密码为'Root56789'.  
    '''
    print("*" * 50)
    print("           小型超市商品信息管理系统          ")
    print("           1.登录;  2.注册;  0.退出.        ")
    print("*" * 50)


    order = eval(input("请输入您要执行的操作指令: "))
    if order == 1:
        uname = input("请输入用户名: ")
        passwd = input("请输入密码: ")
        shop_login(uname, passwd)
    elif order == 2:
        rname = input("请输入您的真实姓名: ")
        phone = input("请输入您的手机号: ")
        shop_reg(uname, passwd, rname phone)
    else:
        pass


def shop_login(uname, passwd):
    '''
    函数功能: 校验输入用户名和密码是否合法
    参数描述: uname 用户名, passwd 密码 
    '''
    if uname == "Root123" and passwd == "Root56789":
        admin()
    elif (uname, passwd):
        cn = check_uname(uname)
        if cn == 1:
            print("用户名格式错误! (只能以大小写字母, 数字, 下划线组成.)")
        elif cn == 2:
            print("用户名不存在! (请先注册再登录)")
        elif cn == 0:
            print("用户名校验无误! ")
        cp = check_passwd(passwd)
            if cp == 1:
                print("密码太长或太短! (密码长度范围为6-18位)")
            elif cp == 2:
                print("密码强度太弱! (密码需要同时包含大小写字母和数字)")
            elif cp == 0:
                print("密码校验成功!")
                return "登录成功!"

def shop_reg(uname, passwd, rname, phone):
    '''
    函数功能: 将从命令行输入的用户名和密码写入数据库的用户表中存储起来, 同时添加用户真实姓名和
    手机号, 便于查询.
    函数参数: uname 用户名 passwd 密码 rname 用户真实姓名 phone 用户手机号
    '''
    reg_result = user_reg(uname, passwd, rname, passwd)

    if  reg_result:
        shop_main()
        return "注册成功!"
    
    return "注册失败"
    





if __name__ == "__main__":
    shop_main()