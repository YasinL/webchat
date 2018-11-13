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

