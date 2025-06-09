from django.db import models

from django.db import models

class ChatLog(models.Model):
    nickname = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
