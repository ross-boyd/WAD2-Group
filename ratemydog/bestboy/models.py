from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name