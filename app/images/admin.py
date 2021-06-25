from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Account, CustomUser, User, Image

# Register your models here.


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = (
        "name",
    )
    list_display = (
        "name",
    )


@admin.register(User)
class _UserAdmin(admin.ModelAdmin):
    fields = (
        "username",
        "account_type",
    )
    list_display = (
        "username",
        "account_type",
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = (
        "user_id",
        "image",
    )
