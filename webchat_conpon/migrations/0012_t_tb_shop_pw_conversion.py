# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-20 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webchat_conpon', '0011_t_tb_shop_coupon_denomination_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_tb_shop',
            name='pw_conversion',
            field=models.CharField(max_length=500, null=True, verbose_name='口令'),
        ),
    ]
