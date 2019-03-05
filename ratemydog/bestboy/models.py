from django.db import models
from ratemydog import settings
# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Dog(models.Model):
    dog_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    BREED_CHOICES = (
        ('UK', 'Unkown'),
        ('GS', 'German Shepherd'),
        ('DM', 'Dobermann'),
        ('DH', 'Dachshund'),
    )
    breed = models.CharField(max_length=20, choices=BREED_CHOICES,
                             default='Unkown')
    rating = models.FloatField(default=0)
    picture = models.ImageField('img', upload_to='MEDIA_ROOT')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


