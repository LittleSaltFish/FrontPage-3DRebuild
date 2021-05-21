from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user,comment
# Register your models here.

ADDITIONAL_FIELDS = ((None, {'fields': ('photo_url','academy','StudentID')}),)

class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS
    add_fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS

admin.site.site_header = '云党建平台-在线校史馆'  # 设置header
admin.site.site_title = '云党建平台-在线校史馆'   # 设置title
admin.site.index_title = '云党建平台-在线校史馆'

admin.site.register(user, UserAdmin)
admin.site.register(comment)
