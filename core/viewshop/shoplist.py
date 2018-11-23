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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from  core.Log import logger


def shopapi(request):
    keyword_id = request.GET.get('keyword_id')
    page = request.GET.get('page')
    if request.method == "GET":
        shoplists = []

        if keyword_id == "nvz1001":
            contact_list = t_tb_shop.objects.filter(shop_category__contains="女装").all().order_by()
            paginator = Paginator(contact_list, 20)  # Show 20 contacts per page
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contacts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contacts = paginator.page(paginator.num_pages)
            json_data = serializers.serialize("json", contacts, ensure_ascii=False)

            for shop in json.loads(json_data):
                # print(shop.get("fields"))
                shoplists.append(shop.get("fields"))

            if page == "1":
                return render(request, "list.html", {'shoplist': shoplists})
            else:

                return HttpResponse(json.dumps(shoplists), content_type='application/json; charset=utf-8')




        elif keyword_id == "nanz1001":
            contact_list = t_tb_shop.objects.filter(shop_category__contains="男装").all().order_by()
            paginator = Paginator(contact_list, 20)  # Show 20 contacts per page
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contacts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contacts = paginator.page(paginator.num_pages)
            json_data = serializers.serialize("json", contacts, ensure_ascii=False)

            for shop in json.loads(json_data):
                # print(shop.get("fields"))
                shoplists.append(shop.get("fields"))

            if page == "1":
                return render(request, "list.html", {'shoplist': shoplists})
            else:

                return HttpResponse(json.dumps(shoplists), content_type='application/json; charset=utf-8')
        elif keyword_id == "hw1001":
            contact_list = t_tb_shop.objects.filter(shop_category__contains="户外").all().order_by()
            paginator = Paginator(contact_list, 20)  # Show 20 contacts per page
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contacts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contacts = paginator.page(paginator.num_pages)
            json_data = serializers.serialize("json", contacts, ensure_ascii=False)

            for shop in json.loads(json_data):
                # print(shop.get("fields"))
                shoplists.append(shop.get("fields"))

            if page == "1":
                return render(request, "list.html", {'shoplist': shoplists})
            else:

                return HttpResponse(json.dumps(shoplists), content_type='application/json; charset=utf-8')
        elif keyword_id == "hw1001":
            contact_list = t_tb_shop.objects.filter(shop_category__contains="户外").all().order_by()
            paginator = Paginator(contact_list, 20)  # Show 20 contacts per page
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contacts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contacts = paginator.page(paginator.num_pages)
            json_data = serializers.serialize("json", contacts, ensure_ascii=False)

            for shop in json.loads(json_data):
                # print(shop.get("fields"))
                shoplists.append(shop.get("fields"))

            if page == "1":
                return render(request, "list.html", {'shoplist': shoplists})
            else:

                return HttpResponse(json.dumps(shoplists), content_type='application/json; charset=utf-8')


        # try:
        #     shopdblists = t_tb_shop.objects.filter(shop_category__contains="男装").values()
        #     for shoplist in  shopdblists:
        #         shoplists.append(shoplist)
        #
        # except BaseException as e:
        #     logger.error(e)
        #     shoplists = 0

    # return HttpResponse(shoplists, content_type='application/json; charset=utf-8')


#
# def  shopapi(request):
#     if request.method == "GET":
#         keyword_id = request.GET.get('keyword_id')
#         page = request.GET.get('page')
#         shoplist = shoplistapi(keyword_id,page)
#
#         return HttpResponse(shoplist, content_type='application/json; charset=utf-8')



if __name__ == '__main__':
    shop = shopapi("nvz1001","2")
    print(shop)











