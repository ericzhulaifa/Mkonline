# _*_ encoding:utf-8 _*_
"""
    用户操作设计，课程运作动态数据 - 可以调用1-用户，2-课程和3-教学机构里的数据内容，避免循环使用数据表
    4 - Operations 运维模块设计
        4.1 UserAsk             用户咨询
        4.2 CourseComments      课程评论
        4.3 UserFavorite        用户收藏
        4.4 UserMessage         用户消息
        4.5 UserCourse          用户学习课程
        4.6 Banner                  轮播图
"""

from datetime import datetime

from django.db import models

from django.contrib.auth import get_user_model    # 由于我们从新定义了UserProfile model，可以使用这个model来避免代码，因为
                                                  # 这个方法可以自动获取user的信息。
from users.models import BaseModel
from apps.courses.models import Course
from users.models import UserProfile

# Create your models here.

# User_Profile = get_user_model()                     # 实例话这个方法


class Banner(BaseModel):
    """
    4.6 Banner                  轮播图
    """
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=200, verbose_name=u"轮播图")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=0, verbose_name=u"播放顺序")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class UserAsk(BaseModel):
    """
    4.1 UserAsk             用户咨询
    """
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{course} ({mobile})".format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    """
     4.2 CourseComments      课程评论
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")  # Get_user_model()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    comments = models.CharField(max_length=200, verbose_name=u"评论内容")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


FAV_TYPE_CHOICES = (
    (1, "课程"),
    (2, "课程机构"),
    (3, "讲师"),
)


class UserFavorite(BaseModel):
    """
    4.3 UserFavorite        用户收藏
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=FAV_TYPE_CHOICES, default=1, verbose_name=u"收藏类型")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(self.user.username, self.fav_id)


class UserMessage(BaseModel):
    """
    4.4 UserMessage         用户消息
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    message = models.CharField(max_length=200, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourses(BaseModel):
    """
    4.5 UserCourse          用户学习课程
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name
