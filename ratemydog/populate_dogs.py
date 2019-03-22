import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ratemydog.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from bestboy.models import Dog, Rating
from bestboy.choices import *


def populate():
    directory = os.getcwd() + "/bestboy/media/dog_pics"

    User = get_user_model()
    try:
        super_user = User.objects.create_superuser(
            username="SUPERUSER", password="123", email="ding@dong.com")
        test_user = User.objects.create_user(
            username="TESTUSER", password="123")
        new_user = User.objects.create_user(
            username="NEWUSER", password="123")
    except:
        super_user = User.objects.get(username="SUPERUSER")
        test_user = User.objects.get(username="TESTUSER")

    comments = get_comments()
    names = get_names()
    breeds = get_breeds()

    for id in range(1, 102):
        save_dog(random.choice(names), id,
                 random.choice(breeds)[0],
                 "dog_pics/dog" + str(id) + ".jpg", super_user)
        rate_dog(id, round(random.uniform(0, 10), 1), random.choice(comments),
                 test_user)


def save_dog(name, dog_id, breed, picture, owner):
    d = Dog.objects.get_or_create(owner=owner, dog_id=dog_id)[0]
    d.name = name
    d.picture = picture
    d.breed = breed
    d.save()


def rate_dog(id, score, comment, user):
    d = Dog.objects.get(dog_id=id)
    d.score += score
    d.votes += 1
    d.average = d.score / d.votes
    d.save()
    
    r = Rating.objects.get_or_create(dog=d, user=user)[0]
    r.score = score
    r.text = comment
    r.save()

    user.last_voted_id += 1
    user.save()

if __name__ == '__main__':

    print("Populating dogs database...")
    populate()
    print("Populated successfully :)\n")
