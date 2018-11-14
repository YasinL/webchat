#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

import core.tb_sdk.top.api
from core.tb_sdk import top
from core.util.dbutil import tb_app_secret
from  core.Log import logger
import  json

tb_appid = tb_app_secret("tk_webchat").tb_secret("tb_appid")
tb_secret = tb_app_secret("tk_webchat").tb_secret("tb_secret")


def search_Shop(search_keyword):
    req = top.api.TbkDgItemCouponGetRequest("gw.api.taobao.com", port=80)
    req.set_app_info(top.appinfo(appkey=str(tb_appid), secret=str(tb_secret)))
        # req.set_app_info(top.appinfo(appkey="25244012",secret="7abdc920daf305056ee20105d4eaed35"))
    req.adzone_id = 186710703
        # req.platform=1
        # req.cat="16,18"
        # req.page_size=1
    req.q=search_keyword
        # req.page_no=1
    try:
        resp = req.getResponse()
        # print(resp)
    except Exception as e:
        logger.error(e)
        resp = 0

    return resp


if __name__ == '__main__':
    test = search_Shop("娇小150cm显高矮个子冬装新款加小码女装马甲背心+针织连衣裙套装")
    print(test)