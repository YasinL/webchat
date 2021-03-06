#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

import core.tb_sdk.top.api
from  core.tb_sdk import top
from  core.util.dbutil import tb_app_secret
from core.tb.tb_search_shop_wl import search_Shop
from  core.Log import logger

tb_appid = tb_app_secret("tk_webchat").tb_secret("tb_appid")
tb_secret = tb_app_secret("tk_webchat").tb_secret("tb_secret")

# shop = search_Shop("娇小150cm显高矮个子冬装新款加小码女装马甲背心+针织连衣裙套装")

# class Change_Key():
#     def __init__(self,search_keyword):
#         self.search_keyword = search_keyword

    #
    # def shop_response(self):
# shop = dict(search_Shop(self.search_keyword))
# shopitem = shop.get("tbk_dg_item_coupon_get_response")
# shop_tbk_coupon = shopitem["results"]["tbk_coupon"][0]
# shop_tbk_coupon_url = shop_tbk_coupon.get("coupon_click_url")
# shop_pict_url = shop_tbk_coupon.get("pict_url")
# shop_title = shop_tbk_coupon.get("title")


def change_Key(search_keyword):
    req = top.api.TbkTpwdCreateRequest("eco.taobao.com", port=443)
    req.set_app_info(top.appinfo(appkey=str(tb_appid), secret=str(tb_secret)))
    shop = dict(search_Shop(search_keyword))
    shopitem = shop.get("tbk_dg_item_coupon_get_response")
    shop_tbk_coupon = shopitem["results"]["tbk_coupon"][0]
    shop_tbk_coupon_url = shop_tbk_coupon.get("coupon_click_url")
    shop_pict_url = shop_tbk_coupon.get("pict_url")
    shop_title = shop_tbk_coupon.get("title")
    req.user_id = "849382036"
    req.text =shop_title
    req.url = shop_tbk_coupon_url
    req.logo = shop_pict_url
    req.ext = "{}"
    try:
        resp = req.getResponse()
        key = resp.get("tbk_tpwd_create_response").get("data").get("model")
        resp = dict(tb_key=key,shop_title=req.text)

    except Exception as e:
        logger.error(e)
        resp = 0

    return resp

if __name__ == '__main__':
    test = change_Key("娇小150cm显高矮个子冬装新款加小码女装马甲背心+针织连衣裙套装")
    print(test)
    # test = dict(shop).get("tbk_dg_item_coupon_get_response")
    # tbk_coupon = test["results"]["tbk_coupon"][0]
    # print(tbk_coupon)
    # print(tbk_coupon.get("coupon_click_url"))