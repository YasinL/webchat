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

req.user_id="849382036"
req.text="少于五个字符字符"
req.url="https://uland.taobao.com/coupon/edetail?e=pxktW1ozKn0GQASttHIRqTsWZUXMLh%2BUBFzeGGeAeG%2BEdvD4wwM%2BY4mUIkLaYNb4QzXTgpeMlmdDtC1mpnfJyMEv3i58F4jS819cieM8MLZTV9TwpZp2XaPekJ9ZWm%2FuiLIAXOTQcgWX%2ByKRY0LlLmMsalgh0Hoh0CHZE4t%2BW2BIH07HK3v5wByk4Acx5KDOX04GfDqhlD6aEFZisbhJn04r5bYnjtyyt0jFpoi9jk0%3D&traceId=0b0b45b015421839656847885e"
req.logo="http://img.alicdn.com/tfscom/i4/2048604677/O1CN011kQ6s0tmxVuVl0Y_!!2048604677.jpg"
req.ext="{}"
try:
	resp= req.getResponse()
	print(resp)
except Exception as e:
	print(e)