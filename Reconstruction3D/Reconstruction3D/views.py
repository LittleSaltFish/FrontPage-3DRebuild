from django.http import HttpResponse
from django.shortcuts import render

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

def signin(request):
    return render(request,"sign-in.html")

def monitor(request):
    return render(request,"Admin-Charts.html")

def database(request):
    return render(request,"Admin-Tables.html")
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)
