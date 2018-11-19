#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"

# import  core.tb_sdk.top.api
import core.tb_sdk.top.api
from  core.tb_sdk import top


req = top.api.TbkItemGetRequest("gw.api.taobao.com",port=80)
req.set_app_info(top.appinfo(appkey="25244012",secret="7abdc920daf305056ee20105d4eaed35"))

def search_shop(keyword):
	req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
	req.q=keyword
	req.cat="16,18"
	# req.itemloc="杭州"
	# req.sort="tk_rate_des"
	# req.is_tmall=False
	# req.is_overseas=False
	# req.start_price=10
	# req.end_price=10
	# req.start_tk_rate=123
	# req.end_tk_rate=123
	req.platform=2
	# req.page_no=123
	req.page_size=100
	try:
		resp= req.getResponse()
		respshop= resp.get("tbk_item_get_response").get("results").get("n_tbk_item")

		print(len(respshop))
	except BaseException as e:
		print(e)

	return  resp

if __name__ == '__main__':
	test = search_shop("")
	print(test)


