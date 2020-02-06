# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/2/1 5:34 下午'

import xadmin

from apps.organization.models import Teacher, CourseOrg, CityDict


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
                    'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points',
                   'click_nums', 'fav_nums', 'add_time']
    list_editable = ['org', 'name', 'work_years', 'work_company', 'work_position']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    list_editable = ['name', 'desc']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city__name', 'add_time']
    list_editable = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    readonly_fields = ('add_time',)
    empty_value_display = '-???-'


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)