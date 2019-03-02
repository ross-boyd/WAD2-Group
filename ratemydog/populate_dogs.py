import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ratemydog.settings')
import django
django.setup()
from bestboy.models import Dog, Test_User


def populate():
    directory = os.getcwd() + "\\bestboy\\media\\bestboy\\dog_pics"
    names = ["Leo", "Ross", "Bruce", "Danny"]
    breeds = ["GS", "DH", "DM"]

    u = create_user("SUPERUSER")
    for id, file in enumerate(os.listdir(directory)):
        if file.endswith(".jpg"):
            save_dog(random.choice(names) + str(id), random.choice(breeds),
                     round(random.uniform(0, 10), 2), directory + file, u)


def save_dog(name, breed, rating, picture, owner):
    d = Dog.objects.get_or_create(name=name, picture=picture)[0]
    d.breed = breed
    d.rating = rating
    d.owner = owner
    d.save()

    return d


def create_user(name):
    u = Test_User.objects.get_or_create(name=name)[0]
    u.save()

    return u

if __name__ == '__main__':
    print("Populating dogs database...")
    populate()
