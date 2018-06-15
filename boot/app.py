#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import web
import hashlib
from wxapi import WXapi
import sys

sys.path.append("..")
import logs.log as Mylog

urls = (
    '/devops', 'WXapi'
)

web.config.debug = True

if __name__ == '__main__':
    log = Mylog.Log
    app_root = os.path.dirname(__file__)
    templates_root = os.path.join(app_root, 'templates')
    render = web.template.render(templates_root)
    web.application(urls, globals()).run(log)
