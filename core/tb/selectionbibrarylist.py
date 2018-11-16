#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

import core.tb_sdk.top.api
from  core.tb_sdk import top
from  core.util.dbutil import tb_app_secret
from  core.Log import logger

tb_appid = tb_app_secret("tk_webchat").tb_secret("tb_appid")
tb_secret = tb_app_secret("tk_webchat").tb_secret("tb_secret")
req = top.api.TbkUatmFavoritesGetRequest("gw.api.taobao.com", port=80)
req.set_app_info(top.appinfo(appkey=str(tb_appid), secret=str(tb_secret)))


req.page_no=1
req.page_size=20
req.fields="favorites_title,favorites_id,type"
req.type=1
try:
	resp= req.getResponse()
	print(resp)
except Exception as e:
	print(e)