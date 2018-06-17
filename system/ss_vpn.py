#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssh as myssh


def restart_ss():
    ip = '*.*.*.*'
    port = 22
    username = 'appuser'
    password = 'passwd'
    execmd = 'sudo /home/dcadmin/restart_ss.sh'
    restart_ss = myssh.ssh_exec_command(ip, port, username, password, execmd)
    return restart_ss


def check_ss():
    ip = '*.*.*.*'
    port = 22
    username = 'appuser'
    password = 'passwd'
    execmd = ' ps -ef |grep -E "UID|servers" |grep -v grep'
    check_ss = myssh.ssh_exec_command(ip, port, username, password, execmd)
    return check_ss
