# -*- coding: utf-8 -*-
__author__ = 'Eric Zhu'
__date__ = '2020/1/31 1:59 下午'

from random import Random

from django.core.mail import send_mail

# from apps.users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def random_str(randomlength=8):
    r_str = ''
    r_chars = 'AaBaCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(r_chars) - 1
    random = Random()
    for i in range(randomlength):
        r_str += r_chars[random.randint(0, length)]
    return r_str


# def send_register_email(email, send_type="register"):
#     email_record = EmailVerifyRecord()
#     random_code = random_str(16)
#     email_record.code = random_code
#     email_record.email = email
#     email_record.send_type = send_type
#     email_record.save()
#
#     email_title = ""
#     email_body = ""
#
#     if send_type == "register":
#         email_title = "注册激活链接"
#         email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(random_code)
#
#         send_status = send_mail(email_title, email_body, EMAIL_FROM, [email],   fail_silently=False,)
#         # send_status = True
#         if send_status:
#             pass
#     elif send_type == "forget":
#         email_title = "密码重置链接"
#         email_body = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(random_code)
#
#         send_status = send_mail(email_title, email_body, EMAIL_FROM, [email],   fail_silently=False,)
#         # send_status = True
#         if send_status:
#             pass






