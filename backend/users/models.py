from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    nickname = models.CharField('닉네임', max_length=50, unique=True)
    # email = models.EmailField('이메일', max_length=255, unique=True, null=True, blank=True, default=None)
    age = models.PositiveIntegerField('나이', null=True, blank=True)
    GENDER_CHOICES = (
        (0, '남자'),
        (1, '여자'),
    )
    gender = models.IntegerField('성별', choices=GENDER_CHOICES, null=True, blank=True)
    
    REQUIRED_FIELDS = ['nickname']  # createsuperuser 시 필수 입력
  
    def __str__(self):
        return self.username
    

class ChatHistory(models.Model):
    nickname = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nickname}의 질문: {self.question[:20]}..."

