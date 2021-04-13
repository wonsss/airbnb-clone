from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):
    """ Conversation Model Definition """
    participants = models.ManyToManyField(
        "users.User", related_name="converstation", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()
        #애는 messages를 가지지 않아. 그런데 클래스 Message는 conversation을 가지고 있어,
        #onversation은 Foreign Key를 가지고 있고, related name은 messages야. 
        #그래서 이것이 이유가 되어서, 지금 Conversation은 self.messages를 갖는거야

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages", on_delete=models.CASCADE)
    #user를 없애면 Message도 없어짐
    conversation = models.ForeignKey("Conversation", related_name="messages",on_delete=models.CASCADE)
    #conversation을 없애면 Message도 없어짐
    
    def __str__(self):
        return f'{self.user} says: {self.message}'