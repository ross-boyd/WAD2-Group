from django.db import models

# Create your models here.


class Test_User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Test_User, on_delete=models.CASCADE, default=1)
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
