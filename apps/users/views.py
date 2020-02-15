from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from pure_pagination import Paginator, PageNotAnInteger

from users.models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, ForgetPwdForm, RegisterForm, ModifyPwdForm, DynamicLoginForm, UploadImageForm
from .forms import UserInfoForm, ChangePwdForm
from utils.email_send import send_register_email
from apps.operations.models import UserFavorite, UserMessage
from apps.organization.models import CourseOrg, Teacher
from apps.courses.models import Course


def message_nums(request):

    if request.user.is_authenticated:
        return {'unread_nums': request.user.usermessage_set.filter(has_read=False).count()}
    else:
        return {}


class MyMessagesView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request, *args, **kwargs):
        my_messages = UserMessage.objects.filter(user=request.user).order_by("-add_time")
        current_page = "mymessages"
        for message in my_messages:
            message.has_read = True
            message.save()

        # 对消息数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(my_messages, per_page=2, request=request)
        messages = p.page(page)

        return render(request, "users/usercenter-message.html", {
            "current_page": current_page,
            "my_messages": messages,
        })


class MyFavCourseView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request, *args, **kwargs):
        current_page = "myfav"
        current_fav_page = "mycourse"
        course_list = []
        fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
        for fav_course in fav_courses:
            try:
                course = Course.objects.get(id=fav_course.fav_id)
                course_list.append(course)
            except Course.DoesNotExist as e:
                pass

        return render(request, "users/usercenter-fav-course.html", {
            "current_page": current_page,
            "current_fav_page": current_fav_page,
            "course_list": course_list,
        })


class MyFavTeacherView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request, *args, **kwargs):
        current_page = "myfav"
        current_fav_page = "myteacher"
        teacher_list = []
        fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
        for fav_teacher in fav_teachers:
            try:
                teacher = Teacher.objects.get(id=fav_teacher.fav_id)
                teacher_list.append(teacher)
            except Teacher.DoesNotExist as e:
                pass

        return render(request, "users/usercenter-fav-teacher.html", {
            "current_page": current_page,
            "current_fav_page": current_fav_page,
            "teacher_list": teacher_list,
        })


class MyFavOrgView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request, *args, **kwargs):
        current_page = "myfav"
        current_fav_page = "myorg"
        org_list = []
        fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        for fav_org in fav_orgs:
            try:
                org = CourseOrg.objects.get(id=fav_org.fav_id)
                org_list.append(org)
            except CourseOrg.DoesNotExist as e:
                pass

        return render(request, "users/usercenter-fav-org.html", {
            "current_page": current_page,
            "current_fav_page": current_fav_page,
            "org_list": org_list,
        })


class MyCourseView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request, *args, **kwargs):
        current_page = "mycourse"
        return render(request, "users/usercenter-mycourse.html", {
            "current_page": current_page,
        })


class ChangePwdView(LoginRequiredMixin, View):
    login_url = "/login/"
    def post(self, request, *args, **kwargs):
        pwd_form = ChangePwdForm(request.POST)
        if pwd_form.is_valid():
            # pwd1 = request.POST.get("password1", "")
            # pwd2 = request.POST.get("password2", "")
            #
            # if pwd1 != pwd2:
            #     return JsonResponse({
            #         "status": "fail",
            #         "msg": "密码不一致"
            #     })
            pwd1 = request.POST.get("password1", "")
            user = request.user
            user.set_password(pwd1)
            user.save()
            # login(request, user)     # 避免修改密码后重新登录

            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse(pwd_form.errors)


class UploadImageView(LoginRequiredMixin, View):
    login_url = "/login"

    def post(self, request, *args, **kwargs):
        # 处理用户上传的头像
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "fail"
            })


class UserInfoView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request, *args, **kwargs):
        current_page = "myinfo"
        return render(request, "users/usercenter-info.html", {
          "current_page": current_page
        })

    def post(self, request, *args, **kwargs):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse(user_info_form.errors, {})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class ResetPwdView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email, "msg": "密码不一致！"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd1)
            user.save()

            return render(request, "login.html")

        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})


class ForgetPWdView(View):
    def get(self, request):
        forgetpwd_form = ForgetPwdForm()
        return render(request, "forgetpwd.html", {"forgetpwd_form": forgetpwd_form})

    def post(self, request):
        forgetpwd_form = ForgetPwdForm(request.POST)
        if forgetpwd_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, "send_success.html")
        else:
            return render(request, "forgetpwd.html", {"forgetpwd_form": forgetpwd_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)         # 如何处理邮箱重复的问题？
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html",
                              {"register_form": register_form,
                               "msg": "用户已经存在！"})
            else:
                pass_word = request.POST.get("password", "")
                user_profile = UserProfile()
                user_profile.username = user_name           # 在注册的时候，也同时将用户名写入邮箱地址。
                user_profile.is_active = False              # 表明用户还未激活
                user_profile.email = user_name
                user_profile.password = make_password(pass_word)
                user_profile.save()

                send_register_email(user_name, "register")
                return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class LoginView(View):
    """
    登录功能开发 - 可以进一步完善 1/31/2020 Eric
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        next = request.GET.get("next", "")
        login_form = DynamicLoginForm()
        return render(request, "login.html", {
            "login_form": login_form,
            "next": next,
            })

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)    # 是Dict字典类型
        if login_form.is_valid():
            user_name = login_form.cleaned_data["username"]
            pass_word = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # 登录成功之后应该怎么返回页面呢？
                    next = request.GET.get("next", "")
                    if next:
                        return HttpResponseRedirect(next)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, 'login.html', {"msg": "用户未激活！"})
            else:
                return render(request, 'login.html', {"msg": "用户名或密码错误！", "long_form": login_form})
        else:
            return render(request, 'login.html', {"login_form": login_form})
