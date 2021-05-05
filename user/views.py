from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from user.models import user,comment
from django.utils import timezone



def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user.objects.create_user(username=name, password=password)
        return HttpResponseRedirect("/user/login/")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        # 验证用户名和密码，通过的话，返回User对象
        user = auth.authenticate(username=name, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "login.html")


def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return HttpResponseRedirect("/")


def admim_charts(request):
    if request.method == "GET" and request.user.is_authenticated:
        return render(request, "Admin-Charts.html")
    else:
        return render(request,"Admin-404.html")


def admim_tables(request):
    if request.method == "GET" and request.user.is_authenticated:
        return render(request, "Admin-Tables.html")
    else:
        return render(request, "Admin-404.html")

def make_comment(request):
    if request.method == "POST":
        comment_content  = request.POST['comment_content']
        user_name=request.POST['user_name']
        user_id_str  = request.POST['user_id']
        user_id  = user.objects.filter(id=user_id_str).first()
        
        comment.objects.create(comment_content=comment_content,comment_hot_rate=0,create_time=timezone.now(),is_delete=False,user_id=user.objects.filter(id=user_id).first(),user_name=user_name)
        return render(request,"BBS.html")
    else:
        return render(request, "Admin-404.html")
