# _*_ encoding:utf-8 _*_
"""
    3-Courses 课程主数据
        3.1 Course              课程基本信息
        3.2 Lesson              章节信息
        3.3 Video               视频
        3.4 CourseResource      课程资源
"""

from django.db import models

from users.models import BaseModel
from apps.organization.models import Teacher, CourseOrg

# Create your models here.

DEGREE_CHOICES = (
    ("cj", "初级"),
    ("zj", "中级"),
    ("gj", "高级"),
)


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u"讲师")
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name=u"课程机构")
    name = models.CharField(max_length=50, verbose_name=u"课程名")     # 所有字段没有特殊指定时，默认为必填项
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=2, verbose_name=u"难度")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    notice = models.CharField(default="", max_length=300, verbose_name=u"课程公告")
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name=u"")
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name=u"课程须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name=u"老师告诉你")

    is_classics = models.BooleanField(default=False, verbose_name=u"是否经典")

    detail = models.TextField(verbose_name=u"课程详情")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    tag = models.CharField(max_length=100, verbose_name=u"标签")

    class Meta:
        verbose_name = u"课程标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    # on_delete 表示对应的外键数据被删除后，当前的数据将如何处理。
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")
    url = models.CharField(max_length=1000, verbose_name=u"访问地址")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"下载地址", max_length=200)

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
