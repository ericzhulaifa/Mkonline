# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from pure_pagination import Paginator, PageNotAnInteger

from apps.organization.models import CourseOrg, CityDict, Teacher
from apps.organization.forms import AddAskForm
from apps.operations.models import UserFavorite
from apps.courses.models import Course


class TeacherDetailView(View):
    def get(self, request, teacher_id, *args, **kwargs):
        teacher_detail = Teacher.objects.get(id=int(teacher_id))
        hot_teachers = Teacher.objects.all().order_by("-click_nums")[:5]
        all_courses = Course.objects.filter(teacher_id=teacher_detail.id)

        has_fav_teacher = False
        has_fav_org = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=teacher_id, fav_type='3'):
                has_fav_teacher = True

            if UserFavorite.objects.filter(user=request.user, fav_id=teacher_detail.org.id, fav_type='2'):
                has_fav_org = True

        # 对课程数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, per_page=3, request=request)
        all_courses = p.page(page)

        return render(request, "organization/teacher-detail.html", {
            "teacher_detail": teacher_detail,
            "all_courses": all_courses,
            "teacher_id": teacher_id,
            "hot_teachers": hot_teachers,
            "has_fav_teacher": has_fav_teacher,
            "has_fav_org": has_fav_org,
        })


class TeachersView(View):
    def get(self, request, *args, **kwargs):
        all_teachers = Teacher.objects.all()
        hot_teachers = Teacher.objects.all().order_by("-click_nums")[:3]

        sort = request.GET.get("sort", "")
        if sort == "hot":
            all_teachers = all_teachers.order_by("-click_nums")

        # 对教师数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_teachers, per_page=2, request=request)
        teachers = p.page(page)

        return render(request, "organization/teachers-list.html", {
            "teachers": teachers,
            "sort": sort,
            "hot_teachers": hot_teachers
        })


class OrgDescView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type='2'):
                has_fav = True

        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgCourseView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type='2'):
                has_fav = True

        all_courses = course_org.course_set.all()

        # 对课程数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, per_page=3, request=request)
        courses = p.page(page)

        return render(request, "org-detail-course.html", {
            "all_courses": courses,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgTeacherView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type='2'):
                has_fav = True
        all_teachers = course_org.teacher_set.all()

        return render(request, "org-detail-teachers.html", {
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgHomeView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "homepage"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type='2'):
                has_fav = True

        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]

        return render(request, "org-detail-homepage.html", {
            "all_courses": all_courses,
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


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
