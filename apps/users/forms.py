# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/1/30 9:27 下午'
"""
"""
from django import forms
from captcha.fields import CaptchaField


# class LoginForm(forms.Form):
#     """
#     这里的username 和 password应该是和login页面上的一致，否则将无法验证，
#     利用form功能设计可以进行在完成网页验证工作之后， 和进行数据库操作之前，在Python&Django代码里完成更完善的数据验证工作
#     """
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True, min_length=5)   # 密码最小长度为5位
#
#
# class RegisterForm(forms.Form):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, min_length=5)  # 密码最小长度为5位
#     captcha = CaptchaField(error_messages={"invalid": u"验证码错误！"})   # 重置系统关于invalid的标准翻译 - 认证码
#     # captcha = CaptchaField()
#
#
# class ForgetPwdForm(forms.Form):
#     email = forms.EmailField(required=True)
#     captcha = CaptchaField(error_messages={"invalid": u"验证码错误！"})
#
#
# class ModifyPwdForm(forms.Form):
#     password1 = forms.CharField(required=True, min_length=5)  # 密码最小长度为5位
#     password2 = forms.CharField(required=True, min_length=5)  # 密码最小长度为5位
