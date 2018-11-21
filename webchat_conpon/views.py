from  core.wx.wx_interactive import weixin_main
from  core.viewshop.shop_sel_lib import shop_sel_lib_list as index
from  core.viewshop.shoplist import shopapi
from  webchat_conpon.models import t_tb_shop
from  webchat_conpon.models import t_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
import json






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

def loadmoretest():
    contact_count = t_test.objects.all().count()
    pagecount= contact_count/10
    pagecount = round(pagecount)

    return pagecount


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


if __name__ == '__main__':
    print(loadmoretest())
