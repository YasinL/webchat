#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"
import xlwt
import xlrd
import pymysql
import re
from  core.util.tb_pw_conversion_util import pw_conversion



db = pymysql.connect(host="", user="webchat", db="", password="@@", port=,charset='utf8')
# 打开数据库连接

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()



readbook = xlrd.open_workbook(r'tb_shop.xls')
sheet = readbook.sheet_by_name("Page1")

nrows = sheet.nrows  # 行
ncols = sheet.ncols  # 列

# print(ncols)


for nrow in range(2,nrows):
    # for ncol in range(ncols):
    commodity_id = sheet.cell(nrow, 0).value
    commodity_name = sheet.cell(nrow, 1).value
    shop_master_map_url = sheet.cell(nrow, 2).value
    shop_detail_url = sheet.cell(nrow, 3).value
    shop_category = sheet.cell(nrow, 4).value
    shop_tbk_url = sheet.cell(nrow, 5).value
    shop_price = sheet.cell(nrow, 6).value
    shop_volume = sheet.cell(nrow, 7).value
    shop_income_ratio = sheet.cell(nrow, 8).value
    shop_commission = sheet.cell(nrow, 9).value
    shop_seller_ww = sheet.cell(nrow, 10).value
    shop_seller_id = sheet.cell(nrow, 11).value
    shop_name = sheet.cell(nrow, 12).value
    platform_type = sheet.cell(nrow, 13).value
    coupon_id = sheet.cell(nrow, 14).value
    coupon_count = sheet.cell(nrow, 15).value
    coupon_surplus = sheet.cell(nrow, 16).value
    coupon_denomination = sheet.cell(nrow, 17).value
    coupon_start_time = sheet.cell(nrow, 18).value
    coupon_end_time = sheet.cell(nrow, 19).value
    coupon_url = sheet.cell(nrow, 20).value
    coupon_extension = sheet.cell(nrow, 21).value

    # coupon_denomination ="满9元减5元"
    # coupon_denomination = coupon_denomination.split("元")

    coupon_denomination_value = re.findall(r"(\d+)元无条件券",coupon_denomination)
    if len(coupon_denomination_value) == 0:
        coupon_denomination_value = re.findall(r".*减(\d+)元", coupon_denomination)

    conversion = pw_conversion(coupon_extension,shop_master_map_url)


    # print(coupon_denomination_value[0])
    # print(shop_tbk_url)
    # 使用 execute()  方法执行 SQL 查询
#     sql = '''insert into webchat_conpon_t_tb_shop (commodity_id,commodity_name,shop_master_map_url,shop_detail_url,shop_category,shop_tbk_utl,shop_price,shop_volume,shop_income_ratio,shop_commission,shop_seller_ww,shop_seller_id,shop_name,platform_type,coupon_id,coupon_count,coupon_surplus,coupon_denomination,coupon_start_time,coupon_end_time,coupon_url,coupon_extension \
# ) value (commodity_id,commodity_name,shop_master_map_url,shop_detail_url,shop_category,shop_tbk_utl,shop_price,shop_volume,shop_income_ratio,shop_commission,shop_seller_ww,shop_seller_id,shop_name,platform_type,coupon_id,coupon_count,coupon_surplus,coupon_denomination,coupon_start_time,coupon_end_time,coupon_url,coupon_extension)'''
#     sql = """insert into webchat_conpon_t_tb_shop (commodity_id,commodity_name,shop_master_map_url,shop_detail_url,shop_category,shop_tbk_url,shop_price,shop_volume,shop_income_ratio,shop_commission,shop_seller_ww,shop_seller_id,shop_name,platform_type,coupon_id,coupon_count,coupon_surplus,coupon_denomination,coupon_start_time,coupon_end_time,coupon_url,coupon_extension)  \
#               value  (%s,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r)""" \
#           % (commodity_id,commodity_name,shop_master_map_url,shop_detail_url,shop_category,shop_tbk_url,shop_price,shop_volume,shop_income_ratio,shop_commission,shop_seller_ww,shop_seller_id,shop_name,platform_type,coupon_id,coupon_count,coupon_surplus,coupon_denomination,coupon_start_time,coupon_end_time,coupon_url,coupon_extension)
    try:
        sql = """insert into webchat_conpon_t_tb_shop (commodity_id,commodity_name,shop_master_map_url,shop_detail_url,shop_category,shop_tbk_url,shop_price,shop_volume,shop_income_ratio,shop_commission,shop_seller_ww,shop_seller_id,shop_name,platform_type,coupon_id,coupon_count,coupon_surplus,coupon_denomination,coupon_start_time,coupon_end_time,coupon_url,coupon_extension,coupon_denomination_value,pw_conversion)  \
                      value  (%s,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r)""" \
                  % (commodity_id,commodity_name,shop_master_map_url,shop_detail_url,shop_category,shop_tbk_url,shop_price,shop_volume,shop_income_ratio,shop_commission,shop_seller_ww,shop_seller_id,shop_name,platform_type,coupon_id,coupon_count,coupon_surplus,coupon_denomination,coupon_start_time,coupon_end_time,coupon_url,coupon_extension,coupon_denomination_value[0],conversion)


        cursor.execute(sql)
        db.commit()


        print("susses")
    except BaseException as e:
        print(e)

# 关闭数据库连接
db.close()