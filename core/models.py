from django.db import models


class TimeStampedModel(models.Model):
    """TimeStampedModel"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # 데이터베이스에 등록되지 않도록 위와 같이 abstract=True 설정해주기
