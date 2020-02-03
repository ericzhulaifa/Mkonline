# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/2/1 5:34 下午'

import xadmin


#
# from apps.courses.models import Course, Lesson, Video, CourseResource
#
#
class GlobalSettings(object):
    site_title = "幕学后台管理系统"
    site_footer = "幕学在线网"
    menu_style = "accordion"

class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

#
# class CourseAdmin(object):
#     list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'teacher', 'students', 'fav_nums',
#                     'image', 'click_nums', 'add_time']
#     search_fields = ['teacher', 'name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
#                      'image', 'click_nums']
#     list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'teacher__name', 'students', 'fav_nums',
#                    'image', 'click_nums', 'add_time']
#     list_editable = ['teacher', 'name', 'desc', 'detail', 'degree', 'learn_times', 'teacher', 'students']
#     readonly_fields = ('add_time',)
#     empty_value_display = '-???-'
#
#
# class LessonAdmin(object):
#     list_display = ['course', 'name', 'add_time']
#     search_fields = ['course', 'name']
#     list_filter = ['course__name', 'name', 'add_time']
#     # date_hierarchy = 'add_time'
#     list_editable = ['course', 'name']
#     readonly_fields = ('add_time',)
#     empty_value_display = '-???-'
#
#
# class VideoAdmin(object):
#     list_display = ['lesson', 'name', 'add_time']
#     search_fields = ['lesson', 'name']
#     list_filter = ['lesson', 'name', 'add_time']
#     list_editable = ['lesson', 'name']
#     readonly_fields = ('add_time',)
#     empty_value_display = '-???-'
#
#
# class CourseResourceAdmin(object):
#     list_display = ['course', 'name', 'download', 'add_time']
#     search_fields = ['course', 'name', 'download']
#     list_filter = ['course', 'name', 'download', 'add_time']
#     list_editable = ['course', 'name', 'download']
#     readonly_fields = ('add_time',)
#     empty_value_display = '-???-'
#
#
# xadmin.site.register(Course, CourseAdmin)
# xadmin.site.register(Lesson, LessonAdmin)
# xadmin.site.register(Video, VideoAdmin)
# xadmin.site.register(CourseResource, CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
