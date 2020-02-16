# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/2/1 5:34 下午'

import xadmin

from apps.operations.models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourses, Banner


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    list_editable = ['name', 'mobile', 'course_name']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user__nick_name', 'course', 'comments', 'add_time']
    list_editable = ['user', 'course', 'comments']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user__nick_name', 'fav_id', 'fav_type', 'add_time']
    list_editable = ['user', 'fav_id', 'fav_type']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    list_editable = ['user', 'message', 'has_read']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


class UserCoursesAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user__nick_name', 'course__name', 'add_time']
    list_editable = ['user', 'course']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    list_editable = ['title', 'image', 'url', 'index']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourses, UserCoursesAdmin)
xadmin.site.register(Banner, BannerAdmin)



