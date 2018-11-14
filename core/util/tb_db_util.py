#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

import json
from core.util.dbutil import dbutil



def tb_secret(tb_appname,tb_field):
    tb_dbutil = dbutil().tb_secret(tb_appname)
    tb_secret = dict(json.loads(tb_dbutil))
    secret = tb_secret.get(tb_field)
    return secret


if __name__ == '__main__':
    test =  tb_secret("tk_webchat","")
    print(test)