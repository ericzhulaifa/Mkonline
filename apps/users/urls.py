# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/2/5 7:32 上午'

from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('info/', views.UserInfoView.as_view(), name='user_info'),
    path('image/upload/', views.UploadImageView.as_view(), name='image_upload'),
    # # ex: /polls/5/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # # ex: /polls/5/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
