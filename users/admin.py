from django.contrib import admin

# Admin 만들어주기, user 모델 만들기, 니꼬가 나중에 설명하기로 함
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass