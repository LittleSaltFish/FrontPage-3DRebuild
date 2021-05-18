from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("MakeComment/", views.make_comment, name="make_comment"),
    # path("charts/", views.admin_charts, name="admin_charts"),
    path("comments/", views.admin_comments, name="admin_comments"),
    path("users/", views.admin_users, name="admin_users"),
    path("LikeComment/", views.like_comment, name="like_comment"),
    path("information/", views.information, name="information"),
    path("mycomment/", views.MyComments, name="MyComments"),
]
