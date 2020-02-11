# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/2/5 7:32 上午'

from django.urls import path

from .views import CourseListView, CourseDetailView, CourseLessonView, CourseCommentsView, CourseVideoView

app_name = 'courses'
urlpatterns = [

    path('list/', CourseListView.as_view(), name='list'),
    path('<int:course_id>/detail/', CourseDetailView.as_view(), name='detail'),
    path('<int:course_id>/lesson/', CourseLessonView.as_view(), name='lesson'),
    path('<int:course_id>/comments/', CourseCommentsView.as_view(), name='comments'),
    path('<int:course_id>/video/<int:video_id>', CourseVideoView.as_view(), name='video'),

]
