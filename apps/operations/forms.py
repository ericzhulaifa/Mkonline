# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/1/30 9:27 下午'
"""
"""
import re

from django import forms

from apps.operations.models import UserFavorite


class UserFavForm(forms.ModelForm):

    class Meta:
        model = UserFavorite
        fields = ["fav_id", "fav_type"]
