# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.backends import ModelBackend
# from django.db.models import Q
# from django.views.generic.base import View
# from django.contrib.auth.hashers import make_password
#
# from apps.users.models import UserProfile, EmailVerifyRecord
# from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
# from utils.email_send import send_register_email
# # Create your views here.
#
#
# class ResetPwdView(View):
#     def get(self, request, reset_code):
#         all_records = EmailVerifyRecord.objects.filter(code=reset_code)
#         if all_records:
#             for record in all_records:
#                 email = record.email
#                 return render(request, "password_reset.html", {"email": email})
#         else:
#             return render(request, "active_fail.html")
#         return render(request, "login.html")
#
#
# class ModifyPwdView(View):
#     def post(self, request):
#         modify_form = ModifyPwdForm(request.POST)
#         if modify_form.is_valid():
#             pwd1 = request.POST.get("password1", "")
#             pwd2 = request.POST.get("password2", "")
#             email = request.POST.get("email", "")
#             if pwd1 != pwd2:
#                 return render(request, "password_reset.html", {"email": email, "msg": "密码不一致！"})
#             user = UserProfile.objects.get(email=email)
#             user.password = make_password(pwd1)
#             user.save()
#
#             return render(request, "login.html")
#
#         else:
#             email = request.POST.get("email", "")
#             return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})
#
#
# class ForgetPWdView(View):
#     def get(self, request):
#         forgetpwd_form = ForgetPwdForm()
#         return render(request, "forgetpwd.html", {"forgetpwd_form": forgetpwd_form})
#
#     def post(self, request):
#         forgetpwd_form = ForgetPwdForm(request.POST)
#         if forgetpwd_form.is_valid():
#             email = request.POST.get("email", "")
#             send_register_email(email, "forget")
#             return render(request, "send_success.html")
#         else:
#             return render(request, "forgetpwd.html", {"forgetpwd_form": forgetpwd_form})
#
#
# class ActiveUserView(View):
#     def get(self, request, active_code):
#         all_records = EmailVerifyRecord.objects.filter(code=active_code)
#         if all_records:
#             for record in all_records:
#                 email = record.email
#                 user = UserProfile.objects.get(email=email)         # 如何处理邮箱重复的问题？
#                 user.is_active = True
#                 user.save()
#         else:
#             return render(request, "active_fail.html")
#         return render(request, "login.html")
#
#
# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserProfile.objects.get(Q(username=username) | Q(email=username))
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None
#
#
# def index(request):
#     return HttpResponse("Hello World.")
#
#
# class RegisterView(View):
#     def get(self, request):
#         register_form = RegisterForm()
#         return render(request, "register.html", {'register_form': register_form})
#
#     def post(self, request):
#         register_form = RegisterForm(request.POST)
#         if register_form.is_valid():
#             user_name = request.POST.get("email", "")
#             if UserProfile.objects.filter(email=user_name):
#                 return render(request, "register.html",
#                               {"register_form": register_form,
#                                "msg": "用户已经存在！"})
#             else:
#                 pass_word = request.POST.get("password", "")
#                 user_profile = UserProfile()
#                 user_profile.username = user_name           # 在注册的时候，也同时将用户名写入邮箱地址。
#                 user_profile.is_active = False              # 表明用户还未激活
#                 user_profile.email = user_name
#                 user_profile.password = make_password(pass_word)
#                 user_profile.save()
#
#                 send_register_email(user_name, "register")
#                 return render(request, "login.html")
#         else:
#             return render(request, "register.html", {"register_form": register_form})
#
#
# class LoginView(View):
#     """
#     登录功能开发 - 可以进一步完善 1/31/2020 Eric
#     """
#     def get(self, request):
#         return render(request, "login.html", {})
#
#     def post(self, request):
#         login_form = LoginForm(request.POST)    # 是Dict字典类型
#         if login_form.is_valid():
#             user_name = request.POST.get("username", "")
#             pass_word = request.POST.get("password", "")
#             user = authenticate(username=user_name, password=pass_word)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return render(request, "index.html")
#                 else:
#                     return render(request, 'login.html', {"msg": "用户未激活！"})
#             else:
#                 return render(request, 'login.html', {"msg": "用户名或密码错误！"})
#         else:
#             return render(request, 'login.html', {"login_form": login_form})
#
#
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request, 'login.html', {"msg": "用户名或密码错误！"})
#     elif request.method == 'GET':
#         return render(request, "login.html", {})
