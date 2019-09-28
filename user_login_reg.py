#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import re

def check_uname(uname):
    '''
    函数功能：校验用户名是否合法
    函数参数：
    uname 待校验的用户名
    返回值：校验通过返回0，校验失败返回非零（格式错误返回1，用户名不存在返回2）
    '''
    # [a-zA-Z0-9_]{6, 15}
    if not re.match("^[a-zA-Z0-9_]{6,15}$", uname):
        return 1

    # 连接数据库
    conn = pymysql.connect("127.0.0.1", "qb", "qjbhave$", "test")

    try:
        with conn.cursor() as cur:  # 获取一个游标对象(Cursor类)，用于执行SQL语句
            # 执行任意支持的SQL语句
            cur.execute("select uname from shop_user where uname=%s", (uname, ))
            # 通过游标获取执行结果
            rows = cur.fetchone()
    finally:
        # 关闭数据库连接
        conn.close()  

    if rowcount == 0:
        return 2

    return 0

def check_passwd(passwd):
    '''
    函数功能：校验用户密码是否合法
    函数参数：
    passwd 待校验的密码
    返回值：校验通过返回0，校验错误返回非零（密码太长或太短返回1，密码安全强度太低返回2）
    '''
    # 连接数据库
    conn = pymysql.connect("127.0.0.1", "qb", "qjbhave$", "test")

    if not (len(passwd) >= 6 and len(passwd) <= 18):
        return 1

    elif not re.match(r'(\w+|\W+)+', passwd):
        return 2

    try:
        with conn.cursor() as cur:  # 获取一个游标对象(Cursor类)，用于执行SQL语句
            # 执行任意支持的SQL语句
            cur.execute("select passwd from shop_user where passwd=%s", (passwd, ))
            # 通过游标获取执行结果
            rows = cur.fetchone()
    finally:
        # 关闭数据库连接
        conn.close()  

    elif rows:
        return 0
 
def user_reg(uname, passwd, rname, phone):
    '''
    函数功能: 校验用户信息是否存在, 如果未注册, 即将用户信息存入数据库
    函数参数:
    uname 用户名 passwd 密码 rname 用户真实姓名 phone 用户手机号
    返回值: 校验通过返回True, 未通过返回Flase
    '''
    # 连接数据库
    conn = pymysql.connect("127.0.0.1", "qb", "qjbhave$", "test")

    try:
        cur = conn.cursor()
        cur.execute("select uid from shop_user where uname=%s", (uanme, ))
        res = cur.rowcount
        cur.close()
    except:    
        if res != 0:
            print("用户名已经被注册!")
            return False
    try:
        cur = conn.cursor()
        cur.execute("insert into shop_user(uname, passwd, rname, phone) values (%s, %s, %s, %s)", (uname, passwd, rname, phone))
        cur.close()
        conn.commit()
    except:
        print("用户注册失败!")
        return False
    
    return True