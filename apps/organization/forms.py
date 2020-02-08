# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/1/30 9:27 下午'
"""
"""
from django import forms

from operations.models import UserAsk


class AddAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ["name", "mobile", "course_name"]

