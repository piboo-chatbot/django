from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('nickname',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nickname',)}),
    )
    list_display = ('username', 'nickname', 'email', 'is_staff', 'is_active')

admin.site.register(User, CustomUserAdmin)
