from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from pure_pagination import Paginator, PageNotAnInteger

from apps.courses.models import Course, CourseTag, CourseResource, Video
from apps.operations.models import UserFavorite, UserCourses, CourseComments


class CourseVideoView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, course_id, video_id, *args, **kwargs):
        """
        获取课程详情
        """
        course_detail = Course.objects.get(id=int(course_id))
        course_detail.click_nums += 1
        course_detail.save()

        course_video = Video.objects.get(id=int(video_id))

        # 查询用户是否已经关联了该课程
        user_courses = UserCourses.objects.filter(user=request.user, course=course_detail)
        if not user_courses:
            user_course = UserCourses(user=request.user, course=course_detail)
            user_course.save()

            course_detail.students += 1
            course_detail.save()

        # 学习过该课程的所有同学
        user_courses = UserCourses.objects.filter(course=course_detail)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
        # related_courses = [user_course.course  for user_course in all_courses if user_course.id != course_detail.id]
        related_courses = []
        for item in all_courses:
            if item.course.id != course_detail.id:
                related_courses.append(item.course)

        course_resources = CourseResource.objects.filter(course=course_detail)

        return render(request, 'courses/course-play.html', {
            "course_detail": course_detail,
            "course_resources": course_resources,
            "related_courses": related_courses,
            "course_video": course_video,
        })


class CourseCommentsView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, course_id, *args, **kwargs):
        """
        获取课程详情
        """
        course_detail = Course.objects.get(id=int(course_id))
        course_detail.click_nums += 1
        course_detail.save()

        comments = CourseComments.objects.filter(course=course_detail)

        # 查询用户是否已经关联了该课程
        user_courses = UserCourses.objects.filter(user=request.user, course=course_detail)
        if not user_courses:
            user_course = UserCourses(user=request.user, course=course_detail)
            user_course.save()

            course_detail.students += 1
            course_detail.save()

        # 学习过该课程的所有同学
        user_courses = UserCourses.objects.filter(course=course_detail)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
        # related_courses = [user_course.course  for user_course in all_courses if user_course.id != course_detail.id]
        related_courses = []
        for item in all_courses:
            if item.course.id != course_detail.id:
                related_courses.append(item.course)

        course_resources = CourseResource.objects.filter(course=course_detail)

        return render(request, 'courses/course-comment.html', {
            "course_detail": course_detail,
            "course_resources": course_resources,
            "related_courses": related_courses,
            "comments": comments,
        })


class CourseLessonView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, course_id, *args, **kwargs):
        """
        获取课程详情
        """
        course_detail = Course.objects.get(id=int(course_id))
        course_detail.click_nums += 1
        course_detail.save()

        # 查询用户是否已经关联了该课程
        user_courses = UserCourses.objects.filter(user=request.user, course=course_detail)
        if not user_courses:
            user_course = UserCourses(user=request.user, course=course_detail)
            user_course.save()

            course_detail.students += 1
            course_detail.save()

        # 学习过该课程的所有同学
        user_courses = UserCourses.objects.filter(course=course_detail)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
        # related_courses = [user_course.course  for user_course in all_courses if user_course.id != course_detail.id]
        related_courses = []
        for item in all_courses:
            if item.course.id != course_detail.id:
                related_courses.append(item.course)

        course_resources = CourseResource.objects.filter(course=course_detail)

        return render(request, 'courses/course-video.html', {
            "course_detail": course_detail,
            "course_resources": course_resources,
            "related_courses": related_courses,
        })


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        """
        获取课程详情
        """
        course_detail = Course.objects.get(id=int(course_id))
        course_detail.click_nums += 1
        course_detail.save()

        # 获取收藏状态
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_detail.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course_detail.course_org.id, fav_type=2):
                has_fav_org = True

        # 通过课程的tag做课程的推荐
        # tag = course_detail.tag
        # related_courses = []        # 初始化为了避免在template中for循环出错-如果没有找到类型的课程的话
        # if tag:                     # 排除掉自身之外多个课程. excluded(id__in=[course_detail.id])
        #     related_courses = Course.objects.filter(tag=tag).exclude(id__in=[course_detail.id])[:3]

        tags = course_detail.coursetag_set.all()
        tag_list = [tag.tag for tag in tags]
        course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course_detail.id)
        related_courses = set()     # 使用set避免重复的值
        for course_tag in course_tags:
            related_courses.add(course_tag.course)

        return render(request, 'courses/course-detail.html', {
            "course_detail": course_detail,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
            "related_courses": related_courses,
        })


class CourseListView(View):
    """
    获取课程列表信息
    """
    def get(self, request, *args, **kwargs):
        all_courses = Course.objects.order_by("-add_time")
        hot_courses = Course.objects.order_by("-click_nums")[:3]

        # 按关键字搜索
        keywords = request.GET.get("keywords", "")
        s_type = "course"
        if keywords:
            all_courses = all_courses.filter(Q(name__icontains=keywords)|Q(desc__icontains=keywords)|Q(detail__icontains=keywords))

        # 对课程进行排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_courses = all_courses.order_by("-students")
        elif sort == "hot":
            all_courses = all_courses.order_by("-click_nums")

        # 对课程列表数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, per_page=3, request=request)
        courses = p.page(page)

        return render(request, "courses/course-list.html", {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses,
            "keywords": keywords,
            "s_type": s_type,
        })
