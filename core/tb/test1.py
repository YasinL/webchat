#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

import core.tb_sdk.top.api
from  core.tb_sdk import top
from  core.util.dbutil import tb_app_secret

tb_appid = tb_app_secret("tk_webchat").tb_secret("tb_appid")
tb_secret = tb_app_secret("tk_webchat").tb_secret("tb_secret")

req=top.api.TbkTpwdCreateRequest("eco.taobao.com",port=443)
req.set_app_info(top.appinfo(appkey=str(tb_appid),secret=str(tb_secret)))

req.user_id="lyq11311"
req.text="少于五个字符字符"
req.url="https://uland.taobao.com/coupon/edetail?e=hDpn8vzciC0GQASttHIRqTsWZUXMLh%2BUBFzeGGeAeG%2BEdvD4wwM%2BY4mUIkLaYNb4QzXTgpeMlmdDtC1mpnfJyMEv3i58F4jS819cieM8MLZTV9TwpZp2XaPekJ9ZWm%2FuiLIAXOTQcgWX%2ByKRY0LlLmMsalgh0Hoh0CHZE4t%2BW2BIH07HK3v5wByk4Acx5KDOX04GfDqhlD6aEFZisbhJn04r5bYnjtyyvaubgwSumtk%3D&traceId=0bb6999915421817471142472e"
req.logo="https://uland.taobao.com"
req.ext="{}"
try:
	resp= req.getResponse()
	print(resp)
except Exception as e:
	print(e)