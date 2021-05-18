from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from user.models import comment
from django.utils import timezone
from django.db import models
from user.models import user as UserModel
# 此处user必须改名，否则imformation处会报错：
# local variable 'user' referenced before assignment

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        message = None
        name = request.POST.get("name")
        password = request.POST.get("password")
        if UserModel.objects.filter(username=name):
            message = "用户名已被使用，换一个吧"
            return render(request, "register.html", {"message": message})
        else:
            flag="True"
            message="注册成功"
            message2="请进一步完善信息"
            UserModel.objects.create_user(username=name, password=password)
            user = auth.authenticate(username=name, password=password)
            auth.login(request, user)
            return render(request, "information.html", {"message": message,"message2": message2,"flag":flag})
            # return HttpResponseRedirect("/user/login/")


def login(request):
    if request.method == "GET":
        return render(request, "login.html", {"message": None})
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        # 验证用户名和密码，通过的话，返回User对象
        user = auth.authenticate(username=name, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            message = "请检查用户名和密码"
            return render(request, "login.html", {"message": message})


def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return HttpResponseRedirect("/")


# def admin_charts(request):
#     if request.method == "GET" and request.user.is_authenticated:
#         return render(request, "Admin-Charts.html")
#     else:
#         return render(request, "Admin-404.html")


def admin_comments(request):
    if request.method == "GET" and request.user.is_authenticated:
        comments = comment.objects.all()
        return render(request, "Admin-Comments.html", {"comments": comments})
    else:
        return render(request, "Admin-404.html")


def admin_users(request):
    if request.method == "GET" and request.user.is_authenticated:
        users = UserModel.objects.all()
        return render(request, "Admin-Users.html", {"users": users})
    else:
        return render(request, "Admin-404.html")


def make_comment(request):
    if request.method == "POST":
        comment_content = (
            request.POST["comment_content"].replace("[", "<").replace("]", ">")
        )
        user_name = request.POST["user_name"]
        user_id_str = request.POST["user_id"]
        user_id = UserModel.objects.filter(id=user_id_str).first()
        user_photo_url = UserModel.objects.values("photo_url").get(id=user_id_str)[
            "photo_url"
        ]

        comment.objects.create(
            comment_content=comment_content,
            comment_hot_rate=0,
            create_time=timezone.now(),
            is_delete=False,
            user_id=user_id,
            user_name=user_name,
            user_photo_url=user_photo_url,
        )
        return HttpResponseRedirect("/BBS")
    else:
        return render(request, "Front-404.html")


def list_comment(request):
    if request.method == "GET" and request.user.is_authenticated:
        comment_by_time = comment.objects.all().order_by("-create_time")[:20]
        comment_by_hot_rate = comment.objects.all().order_by("-comment_hot_rate")[:20]

        # for i in range(len(comment_by_hot_rate)):
        #     id= comment_by_hot_rate[i].user_id_id
        #     print(id)
        #     if UserModel.objects.filter(username=id).is_delete:
        #         comment_by_hot_rate[i].user_id=None

        return render(
            request,
            "BBS.html",
            {"by_time": comment_by_time, "by_hot": comment_by_hot_rate},
        )
    else:
        return render(request, "Front-404.html")


def like_comment(request):
    if request.method == "POST":
        comment_id = request.POST["comment_id"]
        target_comment = comment.objects.get(comment_id=str(comment_id))
        target_comment.comment_hot_rate += 1
        target_comment.save()
        return HttpResponseRedirect("/BBS")
    else:
        return render(request, "Front-404.html")


def information(request):
    if request.method == "POST" and request.user.is_authenticated:
        # print(request.POST)
        message = None
        name = request.POST.get("name")
        password_old = request.POST.get("password_old")
        password_new = request.POST.get("password_new")
        password_verify = request.POST.get("password_verify")
        photo_url = request.POST.get("photo_url")
        email = request.POST.get("email")
        academy = request.POST.get("academy")

        if name != request.user.username and UserModel.objects.filter(username=name):
            flag="False"
            message = "用户名已被使用，换一个吧"
            return render(request, "information.html", {"message": message,"flag":flag})

        if password_old and password_new != password_verify:
            flag="False"
            message = "新旧密码不一致"
            return render(request, "information.html", {"message": message,"flag":flag})

        if password_old and not check_password(password_old,request.user.password):
            flag="False"
            message = "旧密码错误，请重新输入"
            return render(request, "information.html", {"message": message,"flag":flag})

        else:
            flag="True"
            message = "修改成功"
            if email:
                request.user.email = email
            if password_old:
                request.user.password = make_password(password_new)
            request.user.username = name
            request.user.photo_url = photo_url
            request.user.academy = academy
            request.user.save()
            if password_old:
                user = auth.authenticate(username=name, password=password_new)
                auth.login(request, user)
            return render(request, "information.html", {"message": message,"flag":flag})
            # return HttpResponseRedirect("/user/login/")
    elif request.method == "GET" and request.user.is_authenticated:
        return render(request, "information.html")
    else:
        return render(request, "Front-404.html")


def MyComments(request):
    if request.method == "GET" and request.user.is_authenticated:
        comments=comment.objects.filter(user_id_id=request.user.id).order_by("-create_time")
        size=len(comments)
        print(comments)
        return render(request,"MyComments.html",{"comments":comments,"size":size})
