from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField('닉네임', max_length=50, unique=True)
    email = models.EmailField('이메일', max_length=255, unique=True, null=True, blank=True, default=None)
    age = models.PositiveIntegerField('나이', null=True, blank=True)
    GENDER_CHOICES = (
        (0, '남자'),
        (1, '여자'),
    )
    gender = models.IntegerField('성별', choices=GENDER_CHOICES, null=True, blank=True)
    
    REQUIRED_FIELDS = ['nickname']  # createsuperuser 시 필수 입력
  
    def __str__(self):
        return self.username
