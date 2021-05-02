from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from django.contrib.auth.models import User

def home(request):
    return render(request,"index.html")

def zone4(request):
    return render(request,"第四展区.html")

def zone3(request):
    return render(request,"第三展区.html")

def zone2(request):
    return render(request,"第二展区.html")

def zone1(request):
    return render(request,"第一展区.html")

def BBS(request):
    return render(request,"BBS.html")

def monitor(request):
    return render(request,"Admin-Charts.html")

def database(request):
    return render(request,"Admin-Tables.html")

