import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ratemydog.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from bestboy.models import Dog


def populate():

    directory = os.getcwd() + "/bestboy/static/bestboy/img/dog_pics"
    breeds = ["GS", "DH", "DM"]

    User = get_user_model()
    try:
        super_user = User.objects.create_superuser(
            username="SUPERUSER", password="123", email="ding@dong.com")
        test_user = User.objects.create_user(
            username="TESTUSER", password="123")
    except:
        super_user = User.objects.get(username="SUPERUSER")
        test_user = User.objects.get(username="TESTUSER")

    with open('comments.txt', 'r') as f:
        comments = []
        for line in f:
            comments.append(line)
    f.close()

    for id in range(1, 102):
        save_dog("Dog" + str(id), id,
                 random.choice(breeds),
                 round(random.uniform(0, 10), 1),
                 directory + "/dog" + str(id) + ".jpg", super_user)


def save_dog(name, dog_id, breed, rating, picture, owner):

    d = Dog.objects.get_or_create(owner=owner, dog_id=dog_id)[0]
    d.name = name
    d.picture = picture
    d.breed = breed
    d.rating = rating
    d.average = rating
    d.votes = 1
    d.save()

    return d


if __name__ == '__main__':

    print("Populating dogs database...")
    populate()
    print("Populated successfully :)\n")
