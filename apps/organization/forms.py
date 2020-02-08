# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/1/30 9:27 下午'
"""
"""
import re

from django import forms

from apps.operations.models import UserAsk


class AddAskForm(forms.ModelForm):
    # 从新定义Model里的mobile字段，因为在那里无法现在最小长度。
    mobile = forms.CharField(max_length=11, min_length=11, required=True)

    class Meta:
        model = UserAsk
        fields = ["name", "mobile", "course_name"]

    def clean_mobile(self):
        """
        验证手机号码是否合法
        :return:
        """

        mobile = self.cleaned_data["mobile"]
        regex_mobile = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(regex_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")
