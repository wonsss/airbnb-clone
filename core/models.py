from django.db import models

<<<<<<< HEAD
class TimeStampedModel(models.Model):
    """Time Stamped Model"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#meta는 기타사항을 적어주는 것임 위에 indented된 것에 대해서
    class Meta:
        abstract = True

        #앱스트랙트 모델은 model이지만 데이터베이스에 나타나지 않는 model임. 코드에서만 쓰임. 그래서 이것을 추상 모델이라고 부름


=======

class TimeStampedModel(models.Model):
    """TimeStampedModel"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # 데이터베이스에 등록되지 않도록 위와 같이 abstract=True 설정해주기
>>>>>>> fa6c254c8ad9c40b6332389b78c08fb063522724
