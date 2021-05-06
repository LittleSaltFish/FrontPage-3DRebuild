from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from user.models import comment

# Create your views here.

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
