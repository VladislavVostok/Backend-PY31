from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    user_name = models.CharField(max_length=32)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
