from django.db import models

# Create your models here.

class t_wx_secret(models.Model):
    wx_appname=models.CharField(max_length=20,null=True)
    wx_appid=models.CharField(max_length=20,null=True)
    wx_secret=models.CharField(max_length=200,null=True)
    wx_token=models.CharField(max_length=100,null=True)


class t_wx_msg(models.Model):
    wx_msg_type = models.CharField(max_length=20,null=True)
    wx_msg_value = models.CharField(max_length=200,null=True)
    wx_msg_keyword = models.CharField(max_length=100,null=True)


class t_tb_secret(models.Model):
    tb_appname=models.CharField(max_length=20,null=True)
    tb_appid=models.CharField(max_length=20,null=True)
    tb_secret=models.CharField(max_length=200,null=True)
    tb_token=models.CharField(max_length=100,null=True)

class t_tb_shopcategory(models.Model):
    categoryid=models.CharField(max_length=50)
    categorylist=models.CharField(max_length=100)
    categoryurl=models.CharField(max_length=100)


class t_tb_shoplist(models.Model):
    shopid = models.CharField(max_length=50,primary_key=True)

class t_tb_shop(models.Model):
    commodity_id = models.CharField(max_length=50,null=True)
    commodity_name = models.CharField(max_length=200,null=True)
    shop_master_map_url = models.CharField(max_length=200,null=True)
    shop_detail_url = models.CharField(max_length=200,null=True)
    shop_category = models.CharField(max_length=100,null=True)
    shop_tbk_url = models.CharField(max_length=500,null=True)
    shop_price = models.CharField(max_length=50,null=True)
    shop_volume = models.CharField(max_length=50,null=True)
    shop_income_ratio = models.CharField(max_length=50,null=True)
    shop_commission = models.CharField(max_length=50,null=True)
    shop_seller_ww = models.CharField(max_length=50,null=True)
    shop_seller_id = models.CharField(max_length=50,null=True)
    shop_name = models.CharField(max_length=100,null=True)
    platform_type = models.CharField(max_length=50,null=True)
    coupon_id = models.CharField(max_length=100,null=True)
    coupon_count = models.CharField(max_length=50,null=True)
    coupon_surplus = models.CharField(max_length=50,null=True)
    coupon_denomination = models.CharField(max_length=50,null=True)
    coupon_denomination_value = models.CharField(max_length=50,null=True)
    coupon_start_time = models.CharField(max_length=50,null=True)
    coupon_end_time = models.CharField(max_length=50,null=True)
    coupon_url = models.CharField(max_length=500,null=True)
    coupon_extension = models.CharField(max_length=500,null=True)
