# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request, *args, **kwargs):
        return render(request, "org-list.html", {})
