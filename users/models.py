from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    Gender_Male = "male"
    Gender_Female = "female"
    Gender_Other = "other"
    Gender_Choices = (
        (Gender_Male, "male"),
        (Gender_Female, "female"),
        (Gender_Other, "other"),
    )
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_USD = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_USD, "KRW"))

    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        choices=Gender_Choices,
        max_length=10,
    )
    bio = models.TextField(
        default=""
    )  # 내가 models에 뭘 쓰든 장고가 알아서 form을 만들어 줄거임. 그리고 장고는 database에 migration과 함께 이 form에 필요한 정보를 요청할 거임
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)