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


def search_Shop(search_keyword,cat):
    req = top.api.TbkDgMaterialOptionalRequest("gw.api.taobao.com", port=80)

    req.set_app_info(top.appinfo(appkey=str(tb_appid), secret=str(tb_secret)))

    req.start_dsr=30000
    req.page_size=100
    req.page_no=1
    req.platform=2
    # req.end_tk_rate=1234
    # req.start_tk_rate=1234
    # req.end_price=10
    # req.start_price=10
    req.is_overseas="false"
    req.is_tmall="false"
    req.sort="total_sales_des"
    # req.itemloc="杭州"
    req.cat=cat
    req.q=search_keyword
    req.material_id=2836
    req.has_coupon="true"
    # req.ip="13.2.33.4"
    req.adzone_id=186710703
    req.need_free_shipment="true"
    req.need_prepay="true"
    req.include_pay_rate_30="true"
    req.include_good_rate="true"
    req.include_rfd_rate="true"
    req.npx_level=1
    # req.end_ka_tk_rate=1234
    # req.start_ka_tk_rate=1234
    # req.device_encrypt="MD5"
    # req.device_value="xxx"
    # req.device_type="IMEI"
    try:
        resp= req.getResponse()
        # respshop= resp.get("tbk_dg_material_optional_response").get("result_list").get("map_data")
        # print(len(respshop))
        # for  shop in  len(resp):

        # print(resp)
    except Exception as e:
        logger.error(e)

    return  resp

if __name__ == '__main__':
    test = search_Shop("","16,18")
    print(test)