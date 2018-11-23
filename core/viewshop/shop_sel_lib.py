#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"
import os
import hashlib
import json
from core.Log import logger
import django
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
import  django.db.utils
from  core.tb.selectionbibrary import shop_lib

def shop_sel_lib_list(request):
    if request.method == "GET":
        shoplist  = shop_lib()
        shoplist = shoplist.get("tbk_dg_item_coupon_get_response").get("results").get("tbk_coupon")
        return render(request,"index.html",{'shoplist':shoplist})




