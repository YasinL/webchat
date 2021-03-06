"""webchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import webchat_conpon.views as views
from django.conf import settings
from  django.views import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.weixin_main, name='weixin_main'),
    url(r'^index$', views.index, name='index'),
    url(r'^shopapi', views.shopapi, name='shopapi'),
    url(r'^loadmore', views.loadmore, name='loadmore'),
    url(r'^pagecount', views.pagecount, name='pagecount'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }),
]
