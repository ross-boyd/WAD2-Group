from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    last_voted_id = models.IntegerField(default=0)
    current_dog_id = models.IntegerField(default=0)

    objects = CustomUserManager()
