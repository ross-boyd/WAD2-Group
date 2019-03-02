import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ratemydog.settings')
import django
django.setup()
from bestboy.models import Dog
import random


def populate():
    directory = os.getcwd() + "\\bestboy\\media\\bestboy\\dog_pics"
    names = ["Leo", "Ross", "Bruce", "Danny"]
    for file in os.listdir(directory):
        if file.endswith(".jpg"):
            save_dog(random.choice(names), "German Shepherd", random.randint(1,10), directory + file)


def save_dog(name, breed, rating, picture):
    print(picture)
    d = Dog.objects.get_or_create(name=name)[0]
    d.breed = breed
    d.rating = rating
    d.picture = picture

    d.save()
    return d


if __name__ == '__main__':
    print("Populating dogs database...")
    populate()