# _*_ encoding:utf-8 _*_
"""Mkonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.conf.urls import url
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin

from users.views import LoginView, LogoutView, ForgetPWdView, RegisterView, ActiveUserView, ResetPwdView, ModifyPwdView
from organization.views import OrgView
from Mkonline.settings import MEDIA_ROOT


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),    # required by ueditor
    path('captcha/', include('captcha.urls')),

    # 配置上传文件的URL访问路径
    # url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # User Register  process control:
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('active/<str:active_code>', ActiveUserView.as_view(), name="user_active"),
    path('forgetpwd/', ForgetPWdView.as_view(), name="forget_pwd"),
    path('reset/<str:reset_code>', ResetPwdView.as_view(), name="reset_pwd"),
    path('modifypwd/', ModifyPwdView.as_view(), name="modify_pwd"),

    # 机构相关页面
    path('org/', include('organization.urls', namespace='org')),

    # 课程相关页面
    path('course/', include('courses.urls', namespace='courses')),

    # 用户操作相关页面
    path('op/', include('operations.urls', namespace='op')),

    # 用户个人中心
    path('users/', include('users.urls')),


]
