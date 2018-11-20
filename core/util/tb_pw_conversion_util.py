#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

import core.tb_sdk.top.api
from  core.tb_sdk import top
from  core.util.dbutil import tb_app_secret
from  core.Log import logger


tb_appid = tb_app_secret("tk_webchat").tb_secret("tb_appid")
tb_secret = tb_app_secret("tk_webchat").tb_secret("tb_secret")

def pw_conversion(url,shop_map_url):
    req=top.api.TbkTpwdCreateRequest("eco.taobao.com",port=443)
    req.set_app_info(top.appinfo(appkey=str(tb_appid),secret=str(tb_secret)))

    req.user_id="849382036"
    req.text="乐迪园优惠"
    req.url=url
    req.logo=shop_map_url
    req.ext="{}"
    try:
        resp= req.getResponse()
        resp = resp.get("tbk_tpwd_create_response").get("data").get("model")
        print(resp)
    except Exception as e:
        logger.error(e)
        resp = 0

    return  resp