# _*_ encoding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


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
