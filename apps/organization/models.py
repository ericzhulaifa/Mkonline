# _*_ encoding:utf-8 _*_
"""
    2-培训机构和教师主数据
        2.1 CityDict               城市信息
        2.2 CourseOrg              课程机构基本信息
        2.3 Teacher                教师基本信息

"""

from django.db import models

from users.models import BaseModel


# Create your models here.


class CityDict(BaseModel):
    """
    2.1 CityDict               城市信息
    """
    name = models.CharField(max_length=20, verbose_name=u"城市名称")
    desc = models.CharField(max_length=200, verbose_name=u"描述")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


CATEGORY_CHOICES = (
    ("pxjg", "培训机构"),
    ("gx", "高校"),
    ("gr", "个人"),
)


class CourseOrg(BaseModel):
    """
    2.2 CourseOrg              课程机构基本信息
    """
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    tag = models.CharField(default=u"全国知名", max_length=10, verbose_name=u"机构标签")
    category = models.CharField(default="pxjg", max_length=4, choices=CATEGORY_CHOICES, verbose_name=u"机构类别")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面图")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name=u"所在城市")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name        # 必须是必填项字段


class Teacher(BaseModel):
    """
    2.3 Teacher                教师基本信息
    """
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    age = models.IntegerField(default=26, verbose_name=u"年龄")
    image = models.ImageField(upload_to="teacher/%Y/%m", max_length=100, verbose_name=u"头像")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
