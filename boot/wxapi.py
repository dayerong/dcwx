#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import time
import web
from lxml import etree
import auth
import menu
import sys

sys.path.append("..")
import database.db as db
import system.ping as ping
import system.ss_vpn as ssvpn
import system.tcping as tcping


class WXapi:
    def __init__(self):
        self.logger = web.ctx.environ['wsgilog.logger']
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, '../templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "*******"   #我的token
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr

    def POST(self):
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        msgType = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        accessip = web.ctx['ip']
        if msgType == 'text':
            content = xml.find("Content").text
            contentlog = "%s:%s:%s" % (accessip, fromUser, content)
            self.logger.info(contentlog)  # 记录日志文件
            if not db.getuser(fromUser):
                inputempid = content.split(' ')[0]
                try:
                    if db.getempid(inputempid):
                        input_pass = content.split(' ')[1]
                        hash_pass = auth.md5(input_pass)
                        passwdindb = db.getpasswd(inputempid)[0]
                        if hash_pass == passwdindb:
                            db.adduser(fromUser, inputempid)
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Authsuccess())
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Authfailed())
                    else:
                        return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Authcheck())
                except IndexError:
                    return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Authcheck())
            else:
                try:
                    # 普通用户功能权限
                    if content.lower() == 'help' and len(content.split()) == 1:
                        return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Mainmenu())
                    elif content.lower()[0:2] == 'sn' and content.lower()[2] == ' ' and len(content.split()) == 2:
                        sn = content.lower()[2:].strip().upper()
                        return self.render.reply_text(fromUser, toUser, int(time.time()), db.querysn(sn))
                    elif content.lower()[0:2] == 'ip' and content.lower()[2] == ' ' and len(content.split()) == 2:
                        ip = content.lower()[2:].strip().upper()
                        return self.render.reply_text(fromUser, toUser, int(time.time()), db.queryip(ip))
                    elif content.lower()[0:2] == 'wz' and content.lower()[2] == ' ' and len(content.split()) == 2:
                        lc = content.lower()[2:].strip().upper()
                        return self.render.reply_text(fromUser, toUser, int(time.time()), db.querylocation(lc))
                    elif content.lower()[0:6] == 'tcping' and content.lower()[6] == ' ' and len(content.split()) == 3:
                        ip = content.split()[1]
                        port = content.split()[2]
                        return self.render.reply_text(fromUser, toUser, int(time.time()), tcping.portcheck(ip, port))
                    elif content.lower()[0:4] == 'ping' and content.lower()[4] == ' ' and len(content.split()) == 2:
                        ip = content.lower()[4:].strip()
                        status = ping.checkping(ip)
                        if str(status) == '0':
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Pingsuccess(ip))
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Pingfailed(ip))
                    # 管理员功能权限
                    elif content.lower() == 'admin' and len(content.split()) == 1:
                        if db.checkuserisadmin(fromUser)[0] == fromUser:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Adminmenu())
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.IsNotAdmin())
                    elif content.lower() == 'restart vpn' and content.lower()[7] == ' ' and len(content.split()) == 2:
                        if db.checkuserisadmin(fromUser)[0] == fromUser:
                            status = ssvpn.restart_ss()
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.RestartSSVPN())
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.IsNotAdmin())
                    elif content.lower() == 'check vpn' and content.lower()[5] == ' ' and len(content.split()) == 2:
                        if db.checkuserisadmin(fromUser)[0] == fromUser:
                            status = ssvpn.check_ss()
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.ChecktSSVPN(status))
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.IsNotAdmin())
                    elif content.lower()[0:10] == 'restart vm' and content.lower()[7] == ' ' and len(
                            content.split()) == 3:
                        if db.checkuserisadmin(fromUser)[0] == fromUser:
                            ip = content.split()[2]
                            halt_reboot.reboot_vm(ip)
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.RestartVM(ip))
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.IsNotAdmin())
                    elif content.lower()[0:7] == 'halt vm' and content.lower()[4] == ' ' and len(
                            content.split()) == 3:
                        if db.checkuserisadmin(fromUser)[0] == fromUser:
                            ip = content.split()[2]
                            halt_reboot.shutdown_vm(ip)
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.HaltVM(ip))
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.IsNotAdmin())
                    elif content.lower()[0:7] == 'adduser':
                        if db.checkuserisadmin(fromUser)[0] == fromUser:
                            try:
                                if content.lower()[7] == ' ' and len(content.split(' ')) == 3:
                                    newempid = content.split(' ')[1]
                                    newemppass = content.split(' ')[2]
                                    hashnewemppass = auth.md5(newemppass)
                                    if db.getempid(newempid):
                                        return self.render.reply_text(fromUser, toUser, int(time.time()),
                                                                      menu.Emperror(newempid))
                                    else:
                                        db.addemp(newempid, hashnewemppass)
                                        return self.render.reply_text(fromUser, toUser, int(time.time()),
                                                                      menu.Adminsuccess(newempid))
                            except:
                                return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Adminhelp())
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.IsNotAdmin())
                    elif content.lower() == 'show admin' and content.lower()[4] == ' ' and len(content.split()) == 2:
                        if db.checkuserisadmin(fromUser)[0] == fromUser:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), db.queryadmin())
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.IsNotAdmin())
                    elif content.lower() == 'show user' and content.lower()[4] == ' ' and len(content.split()) == 2:
                        if db.checkuserisadmin(fromUser)[0] == fromUser:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), db.queryuser())
                        else:
                            return self.render.reply_text(fromUser, toUser, int(time.time()), menu.IsNotAdmin())
                    else:
                        return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Helpmenu())
                except IndexError:
                    return self.render.reply_text(fromUser, toUser, int(time.time()), menu.Reporterror())
