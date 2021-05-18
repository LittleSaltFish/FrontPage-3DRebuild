"""Reconstruction3D URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
from user.views import list_comment,list_comment_hot

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls, name="admin"),
    path('BBS/', list_comment, name="BBS"),
    path('HotBBS/', list_comment_hot, name="HotBBS"),
    path('zone1/', views.zone1, name="zone1"),
    path('zone2/', views.zone2, name="zone2"),
    path('zone3/', views.zone3, name="zone3"),
    path('zone4/', views.zone4, name="zone4"),
    path('user/', include(('user.urls','user'))),  # 用户url
    path('tinymce/', include('tinymce.urls'))
]
