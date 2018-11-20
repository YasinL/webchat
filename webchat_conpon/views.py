from  core.wx.wx_interactive import weixin_main
from  core.viewshop.shop_sel_lib import shop_sel_lib_list as index
from  core.viewshop.shoplist import shopapi
from  webchat_conpon.models import t_tb_shop
from django.core.paginator import Paginator
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect



def loadmore(request):

    list = t_tb_shop.objects.filter(shop_category__contains="女装").values()
    limit = 5
    paginor = Paginator(list, limit)
    page = request.GET.get('page', 2)
    item_info = paginor.page(page)

    context = {'list': item_info, }
    template = 'test1.html'

    return render(request, template, context)
