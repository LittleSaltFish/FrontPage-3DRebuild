from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("login/", views.login),
    path("register/", views.register),
    path("logout/", views.logout, name="logout"),
    path("comment/", views.make_comment, name="comment"),
    path("charts/", views.admim_charts, name="admim_charts"),
    path("tables/", views.admim_tables, name="admim_tables"),
    path("users/", views.admim_users, name="admim_users"),
]
