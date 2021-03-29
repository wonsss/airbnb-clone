from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    bio = models.TextField(
        default=""
    )  # 내가 models에 뭘 쓰든 장고가 알아서 form을 만들어 줄거임. 그리고 장고는 database에 migration과 함께 이 form에 필요한 정보를 요청할 거임
