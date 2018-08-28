#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssh as myssh


def reboot_vm(vm_ip):
    ip = '192.168.189.99'
    port = 22
    username = 'root'
    password = 'passwd'
    execmd = 'ansible-playbook -b -l ' + vm_ip + ' -t reboot /etc/ansible/playbook/need_shutdown.yml'
    reboot_vm = myssh.ssh_exec_command(ip, port, username, password, execmd)


def shutdown_vm(vm_ip):
    ip = '192.168.189.99'
    port = 22
    username = 'root'
    password = 'passwd'
    execmd = 'ansible-playbook -b -l ' + vm_ip + ' -t poweroff /etc/ansible/playbook/need_shutdown.yml'
    shutdown_vm = myssh.ssh_exec_command(ip, port, username, password, execmd)
