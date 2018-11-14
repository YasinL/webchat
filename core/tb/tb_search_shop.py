#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

# import  core.tb_sdk.top.api
import core.tb_sdk.top.api
from  core.tb_sdk import top


req = top.api.TbkItemGetRequest("gw.api.taobao.com",port=80)
req.set_app_info(top.appinfo(appkey="25244012",secret="7abdc920daf305056ee20105d4eaed35"))


req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
req.q="女装"
req.cat="16,18"
req.itemloc="杭州"
# req.sort="tk_rate_des"
# req.is_tmall=False
# req.is_overseas=False
# req.start_price=10
# req.end_price=10
# req.start_tk_rate=123
# req.end_tk_rate=123
# req.platform=1
# req.page_no=123
# req.page_size=20
try:
	resp= req.getResponse()
	print(resp)
except BaseException as e:
	print(e)