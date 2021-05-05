from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.conf import settings


class user(AbstractUser):
    photo_url = models.CharField(max_length=200, verbose_name="头像url")


class comment(models.Model):

    comment_id = models.IntegerField(verbose_name="评论编号", primary_key=True)
    comment_content = HTMLField(verbose_name="评论内容", max_length=500)
    comment_hot_rate = models.IntegerField(verbose_name="点赞数量")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_delete = models.BooleanField(default=False, verbose_name="删除标记")
    # user_id = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, verbose_name="作者id", on_delete=models.DO_NOTHING
    # )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="作者id",default="-1", on_delete=models.SET_NULL,null=True
    )
    user_name = models.CharField(max_length=200)
    user_photo_url = models.CharField(max_length=200, verbose_name="头像url")
