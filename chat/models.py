from django.db import models
from django.contrib.auth import get_user_model


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(get_user_model())

    def __str__(self):
        return f"{self.name} | {self.members}"


class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.message}"
