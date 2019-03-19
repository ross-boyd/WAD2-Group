from django.db import models
from ratemydog import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone


class Dog(models.Model):
    dog_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    BREED_CHOICES = (
        ('UK', 'Unkown'),
        ('GS', 'Leo has no nuts'),
        ('DM', 'Dobermann'),
        ('DH', 'Dachshund'),
    )
    breed = models.CharField(max_length=20, choices=BREED_CHOICES,
                             default='Unkown')
    rating = models.FloatField(default=0)
    average = models.FloatField(default=0)
    picture = models.ImageField('img', upload_to='bestboy/dog_pics/')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Dog, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.TextField(max_length=3000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
