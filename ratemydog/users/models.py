from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    last_voted_id = models.IntegerField(default=0)
    objects = CustomUserManager()
