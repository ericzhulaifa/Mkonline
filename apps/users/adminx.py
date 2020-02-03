# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/2/1 5:34 下午'

import xadmin

from users.models import UserProfile, EmailVerifyRecord, Banner


class UserProfileAdmin(object):
    list_display = ['username', 'nick_name', 'first_name', 'last_name', 'gender',
                    'birthday', 'mobile', 'email', 'date_joined']
    search_fields = ['username', 'nick_name', 'first_name', 'last_name', 'gender', 'mobile', 'email']
    list_filter = ['username', 'nick_name', 'first_name', 'last_name', 'gender',
                   'birthday', 'mobile', 'email', 'date_joined']
    list_editable = ['username', 'nick_name', 'first_name', 'last_name', 'gender',
                    'birthday', 'mobile', 'email']
    readonly_fields = ('date_joined',)
    empty_value_display = '-???-'

    # 使用field只显示部分信息 或者是 exclude 只不显示部分信息
    fields = ('username', 'nick_name', 'first_name', 'last_name', 'birthday', 'gender',
              'address', 'mobile', 'email', 'is_active', 'is_staff', 'date_joined', 'last_login')
    exclude = ('birthday', 'gender')


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    list_editable = ['code', 'email', 'send_type']
    readonly_fields = ('send_time',)
    empty_value_display = '-???-'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    list_editable = ['title', 'image', 'url', 'index']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
