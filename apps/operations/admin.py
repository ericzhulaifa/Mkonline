from django.contrib import admin

# Register your models here.

# from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse
#
#
# class UserAskAdmin(admin.ModelAdmin):
#     list_display = ['name', 'mobile', 'course_name', 'add_time']
#     search_fields = ['name', 'mobile', 'course_name']
#     list_filter = ['name', 'mobile', 'course_name', 'add_time']
#
#
# class CourseCommentsAdmin(admin.ModelAdmin):
#     list_display = ['user', 'course', 'comments', 'add_time']
#     search_fields = ['user', 'course', 'comments']
#     list_filter = ['user__nick_name', 'course', 'comments', 'add_time']
#
#
# class UserFavoriteAdmin(admin.ModelAdmin):
#     list_display = ['user', 'fav_id', 'fav_type', 'add_time']
#     search_fields = ['user', 'fav_id', 'fav_type']
#     list_filter = ['user__nick_name', 'fav_id', 'fav_type', 'add_time']
#
#
# class UserMessageAdmin(admin.ModelAdmin):
#     list_display = ['user', 'message', 'has_read', 'add_time']
#     search_fields = ['user', 'message', 'has_read']
#     list_filter = ['user', 'message', 'has_read', 'add_time']
#
#
# class UserCourseAdmin(admin.ModelAdmin):
#     list_display = ['user', 'course', 'add_time']
#     search_fields = ['user', 'course']
#     list_filter = ['user__nick_name', 'course__name', 'add_time']
#
#
# admin.site.register(UserAsk, UserAskAdmin)
# admin.site.register(CourseComments, CourseCommentsAdmin)
# admin.site.register(UserFavorite, UserFavoriteAdmin)
# admin.site.register(UserMessage, UserMessageAdmin)
# admin.site.register(UserCourse, UserCourseAdmin)
