from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user,comment
# Register your models here.

ADDITIONAL_FIELDS = ((None, {'fields': ('photo_url','academy')}),)

class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS
    add_fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS

admin.site.register(user, UserAdmin)
admin.site.register(comment)
