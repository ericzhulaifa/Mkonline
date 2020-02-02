# _*_ encoding:utf-8 _*_
"""
    1-用户主数据，基本底层数据表
        1.1 UserProfile             用户信息
        1.2 EmailVerifyRecord       邮箱验证信息
        1.3 Banner                  轮播图
"""

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class UserProfile(AbstractUser):
    """
    1.1 UserProfile             用户信息
    继承系统的用户信息后，再添加本系统需要的扩展用户字段
    """
    nick_name = models.CharField(max_length=50, default=u"", verbose_name=u"昵称")
    birthday = models.DateField(null=True, blank=True, verbose_name=u"生日")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="female", verbose_name=u"性别")
    address = models.CharField(max_length=100, default=u"", verbose_name=u"联系地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号码")
    image = models.ImageField(max_length=100, upload_to="user_image/%Y/%m",
                              default=u"user_image/default.png", verbose_name=u"用户头像")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username


class EmailVerifyRecord(models.Model):
    """
    1.2 EmailVerifyRecord       邮箱验证信息
    """
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register", u"注册"), ("forget", u"忘记密码")),
                                 max_length=10, verbose_name=u"验证码类型")
    # 不要使用now()， 需要在实例化时生成时间
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(BaseModel):
    """
    1.3 Banner                  轮播图
    """
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"播放顺序")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
