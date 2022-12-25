from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_superuser", "is_staff", "is_active")
    list_filter = ("is_superuser", "is_staff", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")


admin.site.register(User, UserAdmin)
