#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"
import  django.db.utils
import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webchat.settings")
django.setup()

from  webchat_conpon.models import t_tb_shop
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from  core.Log import logger


def shoplistapi(keyword_id):
    shoplists = []
    if keyword_id == "nvz1001":
        try:
            shopdblists = t_tb_shop.objects.filter(shop_category__contains="女装").values()[1:20]
            for shoplist in shopdblists:
                shoplists.append(shoplist)

        except BaseException as e:
            logger.error(e)
            print(e)
            shoplists = 0

    elif keyword_id == "nanz1001":
        try:
            shopdblists = t_tb_shop.objects.filter(shop_category__contains="男装").values()
            for shoplist in  shopdblists:
                shoplists.append(shoplist)

        except BaseException as e:
            logger.error(e)
            shoplists = 0

    else:
        shoplists = 0



    return  shoplists



def  shopapi(request):
    if request.method == "GET":
        keyword_id = request.GET.get('keyword_id')
        shoplist = shoplistapi(keyword_id)
        if shoplist == 0:
            shoplist = "服务器升级中…… 请稍后再试。"
            return  render(request,"error.html",{'shoplist':shoplist})

        else:
            return render(request, "list.html", {'shoplist': shoplist})



if __name__ == '__main__':
    shop = shoplistapi("nvz1001")
    print(shop)











