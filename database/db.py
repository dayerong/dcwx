#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 连接参数
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'Daphne@1234',
    'db': 'cmdb',
    'charset': 'utf8'
}


def querysn(sn):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select vendor,device,ip,location,status,endtime from hardwareinfo where sn=\'%s\'" % sn
        cursor.execute(sql)
        rows = int(cursor.rowcount)
        if rows == 0:
            return "未查询到该SN信息"
        else:
            for i in range(rows):
                row = cursor.fetchone()
                return """
    品牌：%s
    设备名称：%s
    IP地址：%s
    机柜位置：%s
    维保状态：%s
    截止时间：%s""" % (row[0], row[1], row[2], row[3], row[4], row[5])
    finally:
        cursor.close()
        conn.close()


def queryip(ip):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select vendor,device,sn,location,status,endtime from hardwareinfo where ip=\'%s\'" % ip
        cursor.execute(sql)
        rows = int(cursor.rowcount)
        if rows == 0:
            sql = "select appname,vmname,ip,cpu,memory,os from vminfo where ip=\'%s\'" % ip
            cursor.execute(sql)
            rows = int(cursor.rowcount)
            if rows == 0:
                return "未查询到该IP信息"
            else:
                for i in range(rows):
                    row = cursor.fetchone()
                    return """
        应用系统：%s
        VM名称：%s
        IP：%s
        CPU：%s
        内存：%s MB
        OS：%8s """ % (row[0], row[1], row[2], row[3], row[4], row[5])
        else:
            for i in range(rows):
                row = cursor.fetchone()
                return """
    品牌：%s
    设备名称：%s
    序列号：%s
    机柜位置：%s
    维保状态：%s
    截止时间：%s""" % (row[0], row[1], row[2], row[3], row[4], row[5])
    finally:
        cursor.close()
        conn.close()


def querylocation(lc):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select vendor,device,sn,ip,status,endtime from hardwareinfo where location=\'%s\'" % lc
        cursor.execute(sql)
        rows = int(cursor.rowcount)
        if rows == 0:
            return "未查询到该位置信息"
        else:
            for i in range(rows):
                row = cursor.fetchone()
                return """
    品牌：%s
    设备名称：%s
    序列号：%s
    IP地址：%s
    维保状态：%s
    截止时间：%s""" % (row[0], row[1], row[2], row[3], row[4], row[5])
    finally:
        cursor.close()
        conn.close()


def getempid(empid):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select empid from auth where empid = \'%s\'" % empid
        cursor.execute(sql)
        rows = int(cursor.rowcount)
        if rows == 0:
            return ''
        else:
            for i in range(rows):
                row = cursor.fetchone()
                return row
    finally:
        cursor.close()
        conn.close()


def getpasswd(empid):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select password from auth where empid = \'%s\'" % empid
        cursor.execute(sql)
        rows = int(cursor.rowcount)
        if rows == 0:
            return 'None'
        else:
            for i in range(rows):
                row = cursor.fetchone()
                return row
    finally:
        cursor.close()
        conn.close()


def adduser(user, empid):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        # sql = "update touser set toUser=%s, status=0 where empid=%s" %(user, empid)
        sql = "insert into touser(toUser,status,empid) values(\'%s\',0,\'%s\')" % (user, empid)
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def getuser(touser):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select toUser from touser where toUser=\'%s\'" % touser
        cursor.execute(sql)
        rows = int(cursor.rowcount)
        if rows == 0:
            return ''
        else:
            for i in range(rows):
                row = cursor.fetchone()
                return row
    finally:
        cursor.close()
        conn.close()


def addemp(empid, password):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "insert into auth(empid,status,password,admin) values(\'%s\',0,\'%s\',0)" % (empid, password)
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def checkadmin(empid):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select admin from auth where empid = \'%s\'" % empid
        cursor.execute(sql)
        rows = int(cursor.rowcount)
        if rows == 0:
            return 'None'
        else:
            for i in range(rows):
                row = cursor.fetchone()
                return row
    finally:
        cursor.close()
        conn.close()
