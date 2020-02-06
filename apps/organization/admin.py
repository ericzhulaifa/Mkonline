# from django.contrib import admin
#
# # Register your models here.
#
# from .models import CityDict, CourseOrg, Teacher
#
#
# class CityDictAdmin(admin.ModelAdmin):
#     list_display = ['name', 'desc', 'add_time']
#     search_fields = ['name', 'desc']
#     list_filter = ['name', 'desc', 'add_time']
#
#
# class CourseOrgAdmin(admin.ModelAdmin):
#     list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
#     search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
#     list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city__name', 'add_time']
#
#
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
#                     'click_nums', 'fav_nums', 'add_time']
#     search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
#     list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points',
#                    'click_nums', 'fav_nums', 'add_time']
#
#
# admin.site.register(CityDict, CityDictAdmin)
# admin.site.register(CourseOrg, CourseOrgAdmin)
# admin.site.register(Teacher, TeacherAdmin)
#
