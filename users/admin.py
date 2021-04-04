<<<<<<< HEAD
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
=======
from django.contrib import admin

# 아래줄은 어떻게 술술 쓰는거지?
from django.contrib.auth.admin import UserAdmin

# Admin 만들어주기, user 모델 만들기, 니꼬가 나중에 설명하기로 함
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ custom user admin """

    # UserAdmin.fieldsets과 custom profile 필드셋 합치기
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
>>>>>>> fa6c254c8ad9c40b6332389b78c08fb063522724
