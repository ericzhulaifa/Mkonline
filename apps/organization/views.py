# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from pure_pagination import Paginator, PageNotAnInteger

from apps.organization.models import CourseOrg, CityDict
from apps.organization.forms import AddAskForm

# Create your views here.


class AddAskView(View):
    """
    处理用户咨询
    """
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "添加出错"
            })


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据
        all_orgs = CourseOrg.objects.all()
        all_cities = CityDict.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        # 通过机构类别对课程机构进行筛选
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 通过所在城市对课程机构进行筛选
        city_id = request.GET.get("city", "")
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对机构进行排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_orgs = all_orgs.order_by("-students")
        elif sort == "courses":
            all_orgs = all_orgs.order_by("-course_nums")

        org_nums = all_orgs.count()

        # 对课程机构数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, per_page=3, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "org_nums": org_nums,
            "all_cities": all_cities,
            "category": category,
            "city_id": city_id,
            "sort": sort,
            "hot_orgs": hot_orgs,
        })
