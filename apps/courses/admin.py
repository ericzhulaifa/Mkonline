from django.contrib import admin

# Register your models here.

# from .models import Course, Lesson, Video, CourseResource
#
#
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
#                     'image', 'click_nums', 'add_time']
#     search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
#                      'image', 'click_nums']
#     list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
#                    'image', 'click_nums', 'add_time']
#
#
# class LessonAdmin(admin.ModelAdmin):
#     list_display = ['course', 'name', 'add_time']
#     search_fields = ['course', 'name']
#     list_filter = ['course__name', 'name', 'add_time']
#     # date_hierarchy = 'add_time'
#
#
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ['lesson', 'name', 'add_time']
#     search_fields = ['lesson', 'name']
#     list_filter = ['lesson', 'name', 'add_time']
#
#
# class CourseResourceAdmin(admin.ModelAdmin):
#     list_display = ['course', 'name', 'download', 'add_time']
#     search_fields = ['course', 'name', 'download']
#     list_filter = ['course', 'name', 'download', 'add_time']
#
#
# admin.site.register(Course, CourseAdmin)
# admin.site.register(Lesson, LessonAdmin)
# # admin.site.register(Lesson)               #仅仅显示内容的话，可以直接使用内置的方法
# admin.site.register(Video, VideoAdmin)
# admin.site.register(CourseResource, CourseResourceAdmin)
