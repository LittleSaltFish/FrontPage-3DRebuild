from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.conf import settings

class user(AbstractUser):
    phone_number = models.CharField(max_length=20)


class comment(models.Model):

    comment_id = models.IntegerField(verbose_name="评论编号", primary_key=True)
    comment_introduction = HTMLField(verbose_name="评论内容", max_length=500)
    comment_hot_rate = models.IntegerField(verbose_name="评论热度")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="作者姓名", default="-1", on_delete=models.SET("已注销")
    )

