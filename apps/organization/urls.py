# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/2/5 7:32 上午'

from django.urls import path

from .views import OrgView, AddAskView, OrgHomeView


app_name = 'organization'
urlpatterns = [
    path('list/', OrgView.as_view(), name='list'),
    path('add_ask/', AddAskView.as_view(), name='add_ask'),

    path('<int:org_id>/', OrgHomeView.as_view(), name='org_home')
]
