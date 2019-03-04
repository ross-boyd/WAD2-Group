import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ratemydog.settings')
import django
django.setup()
from bestboy.models import Dog
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def populate():
    directory = os.getcwd() + "\\bestboy\\media\\bestboy\\dog_pics"
    names = ["Leo", "Ross", "Bruce", "Danny"]
    breeds = ["GS", "DH", "DM"]

    User = get_user_model()
    try:
        super_user = User.objects.create_user(username="SUPERUSER")
        test_user = User.objects.create_user(username="TESTUSER")
    except:
        super_user = User.objects.get(username="SUPERUSER")
        test_user = User.objects.get(username="TESTUSER")

    for id, file in enumerate(os.listdir(directory)):
        if file.endswith(".jpg"):
            save_dog(random.choice(names) + str(id), id, random.choice(breeds),
                     round(random.uniform(0, 10), 1),
                     directory + file, super_user)


def save_dog(name, dog_id, breed, rating, picture, owner):
    d = Dog.objects.get_or_create(owner=owner, dog_id=dog_id)[0]
    d.name = name
    d.picture = picture
    d.breed = breed
    d.rating = rating
    d.save()

    return d


def create_user(name):
    u = Test_User.objects.get_or_create(name=name)[0]
    u.save()

    return u

if __name__ == '__main__':
    print("Populating dogs database...")
    populate()
