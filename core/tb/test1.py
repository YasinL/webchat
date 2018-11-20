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
req.text="乐迪园优惠"
req.url="https://uland.taobao.com/coupon/edetail?e=W6zYp5G3UUkGQASttHIRqZH95sIFmk6RYrpNo33QiALSJ8DRB%2BFABUvIfiu4py4dblLPySRnkbKhfM%2FuyDq35meqIdvAqY1Z819cieM8MLZTV9TwpZp2XaPekJ9ZWm%2FuiLIAXOTQcgWX%2ByKRY0LlLmMsalgh0Hoh0CHZE4t%2BW2DnbYfZPG6qkhyk4Acx5KDO100AtL32rujZeF9VVoymoZF6FQGnxA7X%2FcHPSv%2BfS9U%3D&traceId=0b0fa66e15424555259081926e"
req.logo="http://img.alicdn.com/tfscom/i4/2048604677/O1CN011kQ6s0tmxVuVl0Y_!!2048604677.jpg"
req.ext="{}"
try:
	resp= req.getResponse()
	print(resp)
except Exception as e:
	print(e)
