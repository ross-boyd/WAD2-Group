from django.db import models
from ratemydog import settings
# Create your models here.
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    User = get_user_model()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_voted_id = models.IntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


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
