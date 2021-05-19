from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from user.models import comment

# Create your views here.


def home(request):
    return render(request, "index.html")


def article3(request):
    return render(request, "3-师生成果.html")


def article2(request):
    return render(request, "2-建设成就.html")


def article1(request):
    return render(request, "1-发展历程.html")


def article0(request):
    return render(request, "0-操作指南.html")
