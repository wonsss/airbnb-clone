from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Admin 만들어주기, user 모델 만들기, 니꼬가 나중에 설명하기로 함
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ custom user admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
