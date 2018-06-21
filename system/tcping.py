#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


def portcheck(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        rs = sock.connect_ex((ip, int(port)))
        return "【%s:%s】 Port is open!" % (ip, port)
    except:
        return "【%s:%s】 Port is down!" % (ip, port)
    finally:
        sock.close()
