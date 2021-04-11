from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):
    """ Conversation Model Definition """
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return self.created


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    #user를 없애면 Message도 없어짐
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)
    #conversation을 없애면 Message도 없어짐
    
    def __str__(self):
        return f'{self.user} says: {self.text}'