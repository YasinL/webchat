from  core.wx.wx_interactive import weixin_main
from  core.viewshop.shop_sel_lib import shop_sel_lib_list as index
from  core.viewshop.shoplist import shopapi
from  webchat_conpon.models import t_tb_shop
from  webchat_conpon.models import t_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
import json
from django.core import serializers





# def loadmore(request):
#     if request.method == "GET":
#         page = request.GET.get('page')
#
#         list = t_tb_shop.objects.filter(shop_category__contains="女装").values()
#         limit = 15
#         paginor = Paginator(list, limit)
#         item_info = paginor.page(page)
#         context = {'list': item_info, }
#         template = 'test1.html'
#
#         return render(request, template, context)

def pagecount(request):
    pagecounts = []
    classify = request.GET.get('classify')
    if classify == "nvz1001":
        try:
            contact_count = t_tb_shop.objects.filter(shop_category__contains="女装").count()
            print(contact_count)
            pagecount= contact_count/20
            pagecount = round(pagecount)
        except BaseException as e:
            print(e)
            pagecount = 1
    elif classify == "nanz1001":
        try:
            contact_count = t_tb_shop.objects.filter(shop_category__contains="男装").count()
            pagecount= contact_count/20
            pagecount = round(pagecount)

        except BaseException as e:
            print(e)
            pagecount = 1





    return HttpResponse(pagecount)


def loadmore(request):
    contact_list = t_test.objects.all()
    paginator = Paginator(contact_list, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    if page == "1":
        return render(request, 'test2.html', {'contacts': contacts})
    else:
        shoplists = []
        shopdblists = t_test.objects.all()[0:20]
        for shoplist in shopdblists:
            test = dict(commodity_name=shoplist.commodity_name)
            shoplists.append(test)
        print(shoplists)

        return HttpResponse(json.dumps(shoplists, ensure_ascii=False), content_type="application/json")



def test(page):
    contact_list = t_tb_shop.objects.filter(shop_category__contains="女装").all().order_by()
    paginator = Paginator(contact_list, 20)  # Show 20 contacts per page
    shoplists =[]
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    json_data = serializers.serialize("json", contacts, ensure_ascii=False)
    return HttpResponse(json_data, content_type='application/json; charset=utf-8')

    # for shop in  contacts:
    #     test = dict(commodity_name=shop.commodity_name)
    #     shoplists.append(test)



if __name__ == '__main__':
    print(test(2))
