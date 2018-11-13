#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

import django
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
import  django.db.utils
import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webchat.settings")
django.setup()
from  webchat_conpon.models import t_tb_secret
from  webchat_conpon.models import t_tb_shopcategory
from  webchat_conpon.models import t_tb_shoplist
from  webchat_conpon.models import t_wx_msg
from  webchat_conpon.models import t_wx_secret

from  core.Log import logger


class dbutil():
    def wx_secret(self,wx_appname):
        try:
            wx_secret = t_wx_secret.objects.filter(wx_appname__exact=wx_appname).values()
            for wx_values in wx_secret:
             wx_secret_dict = dict(wx_appname=wx_values['wx_appname'], wx_appid=wx_values['wx_appid'],
                                          wx_secret=wx_values['wx_secret'], wx_token=wx_values['wx_token'])
             wx_secret_dict = wx_secret_dict
        except BaseException as e:
            logger.error(e)
            wx_secret_dict = 0

        return json.dumps(wx_secret_dict)


    def tb_secret(self,tb_appname):
        try:
            tb_secret = t_tb_secret.objects.filter(wx_appname__exact=tb_appname).values()
            for tb_values in tb_secret:
             tb_secret_dict = dict(wx_appname=tb_values['wx_appname'], wx_appid=tb_values['wx_appid'],
                                          wx_secret=tb_values['wx_secret'], wx_token=tb_values['wx_token'])
             tb_secret_dict = tb_secret_dict
        except BaseException as e:
            logger.error(e)
            tb_secret_dict = 0

        return json.dumps(tb_secret_dict)


    def wx_msg(self,wx_msg_type):
        try:
            tb_secret = t_tb_secret.objects.filter(wx_appname__exact=wx_msg_type).values()
            for tb_values in tb_secret:
             tb_secret_dict = dict(wx_appname=tb_values['wx_appname'], wx_appid=tb_values['wx_appid'],
                                          wx_secret=tb_values['wx_secret'], wx_token=tb_values['wx_token'])
             tb_secret_dict = tb_secret_dict
        except BaseException as e:
            logger.error(e)
            tb_secret_dict = 0

        return json.dumps(tb_secret_dict)


if __name__ == '__main__':
    wx_appname = 'webchat_tb'
    wx_dbutil  = dbutil()
    print(wx_dbutil.wx_secret(wx_appname))


