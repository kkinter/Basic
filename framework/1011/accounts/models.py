from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# DB에 이미 모델이 있음 >> 클래스 상속 받아서 모델 정의
class User(AbstractUser):
    pass