#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

import core.tb_sdk.top.api
from  core.tb_sdk import top
from  core.util.dbutil import tb_app_secret
import json
from  core.Log import logger

tb_appid = tb_app_secret("tk_webchat").tb_secret("tb_appid")
tb_secret = tb_app_secret("tk_webchat").tb_secret("tb_secret")

def shop_lib():
    req = top.api.TbkDgItemCouponGetRequest("gw.api.taobao.com", port=80)
    req.set_app_info(top.appinfo(appkey=str(tb_appid), secret=str(tb_secret)))

    req.platform=1
    req.page_size=1
    req.adzone_id=186710703
    req.unid="2018111718"
    req.favorites_id=18862688
    req.page_no=2
    req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick,shop_title,zk_final_price_wap,event_start_time,event_end_time,tk_rate,status,type"
    try:
        resp= req.getResponse()
        print(type(resp))
        # resp =
        # resp
    except Exception as e:
        print(e)


    return resp


if __name__ == '__main__':
    print(shop_lib())