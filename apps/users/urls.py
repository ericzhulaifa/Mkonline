# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/2/5 7:32 上午'

from django.urls import path
# from django.views.generic import TemplateView

from .views import UserInfoView, UploadImageView, ChangePwdView, MyCourseView, MyFavOrgView, MyFavCourseView
from .views import MyFavTeacherView, MyMessagesView
# from django.contrib.auth.decorators import login_required

app_name = 'users'
urlpatterns = [
    path('info/', UserInfoView.as_view(), name='user_info'),
    path('image/upload/', UploadImageView.as_view(), name='image_upload'),
    path('update/pwd/', ChangePwdView.as_view(), name='update_pwd'),
    path('mycourse/', MyCourseView.as_view(), name='mycourse'),
    # path('mycourse/', login_required(TemplateView.as_view(template_name="users/usercenter-mycourse.html"), login_url="/login/"), {"current_page": "mycourse"}, name='mycourse'),
    path('myfavorg/', MyFavOrgView.as_view(), name='myfavorg'),
    path('myfavteacher/', MyFavTeacherView.as_view(), name='myfavteacher'),
    path('myfavcourse/', MyFavCourseView.as_view(), name='myfavcourse'),
    path('mymessages/', MyMessagesView.as_view(), name='mymessages'),

]
