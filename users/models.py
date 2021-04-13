from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    details         = models.TextField(max_length=150, blank=True)
    profile_picture = models.ImageField(upload_to='uploads/', blank=True)

    articles        = models.IntegerField(default=0)
    likes           = models.IntegerField(default=0)
    views           = models.IntegerField(default=0)
    balance         = models.IntegerField(default=0)
    verified        = models.BooleanField(default=False)
    is_lipikar      = models.BooleanField(default=False)