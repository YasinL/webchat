# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-13 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webchat_conpon', '0005_t_wx_msg_wx_msg_keyword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_tb_secret',
            old_name='wx_appid',
            new_name='tb_appid',
        ),
        migrations.RenameField(
            model_name='t_tb_secret',
            old_name='wx_appname',
            new_name='tb_appname',
        ),
        migrations.RenameField(
            model_name='t_tb_secret',
            old_name='wx_secret',
            new_name='tb_secret',
        ),
        migrations.RenameField(
            model_name='t_tb_secret',
            old_name='wx_token',
            new_name='tb_token',
        ),
    ]
