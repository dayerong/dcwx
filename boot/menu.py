#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def Mainmenu():
    return """请选择（输入忽略大小写）：
■  按【SN】查询
    例：【sn 06WXN36】

■  按【IP】查询
    例：【ip 192.168.0.12】

■  按【机柜位置】查询
    例：【wz 1-22-24-24】
    表示‘机房编号-机柜号-U位置(下)-U位置(上)’
    主机房:1，测试机房:2，网络机房:3，小机房:4

■  【ping测试】
     例：【ping 192.168.0.12】

■  【端口测试】
     例：【tcping 192.168.0.12 80】

■  管理员入口
   【admin】"""


def Helpmenu():
    return "无效指令！请输入【help】，按提示选择！"


def Authcheck():
    return '未被授权，请输入授权账户与密码！【工号+空格+密码】'


def Authsuccess():
    return "密码正确，已授权！ 输入【help】查看功能帮助。"


def Authfailed():
    return "密码错误！请重新输入！"


def Reporterror():
    return "指令格式错误！输入【help】查看功能帮助。"


def Adminmenu():
    return """管理员权限指令：
■  添加用户
    【adduser+空格+新建工号+空格+密码】
    例：【adduser 10001 password】

■  查看用户
    【show user】

■  查看管理员
    【show admin】

■  重启ShadowSocks服务
    【restart vpn】

■  查询ShadowSocks进程
    【check vpn】

■  重启服务器系统
    【restart vm 192.168.0.12】

■  关闭服务器系统
    【halt vm 192.168.0.12】"""


def Adminhelp():
    return "指令格式错误！输入【admin】查看功能帮助。"


def Adminsuccess(empid):
    return "工号【%s】创建成功。" % empid


def Emperror(empid):
    return "工号【%s】已存在。" % empid


def Pingsuccess(ip):
    return "【%s】Ping successful!" % ip


def Pingfailed(ip):
    return "【%s】Ping failed!" % ip


def RestartSSVPN():
    return "shadowsocks已重启！"


def ChecktSSVPN(status):
    return """shadowsocks进程状态：
%s""" % status


def RestartVM(ip):
    return "【%s】正在重启！" % ip


def HaltVM(ip):
    return "【%s】正在关闭！" % ip


def IsNotAdmin():
    return "非管理员，无权限操作！"
