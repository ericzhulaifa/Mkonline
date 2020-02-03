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
from django.urls import include, path

import xadmin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),    # required by ueditor
    path('captcha/', include('captcha.urls')),

    # User Register process control:
    # path('login/', LoginView.as_view(), name="login"),
    # path('register/', RegisterView.as_view(), name="register"),
    # path('active/<str:active_code>', ActiveUserView.as_view(), name="user_active"),
    # path('forgetpwd/', ForgetPWdView.as_view(), name="forget_pwd"),
    # path('reset/<str:reset_code>', ResetPwdView.as_view(), name="reset_pwd"),
    # path('modifypwd/', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构首页
    # path('org_list/', OrgView.as_view(), name="org_list"),

]
