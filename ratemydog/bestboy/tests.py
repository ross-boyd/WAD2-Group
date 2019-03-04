from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from django.contrib.staticfiles import finders
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Checks whether urls are loaded successfully.


class UrlTests(TestCase):

    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vote(self):
        url = reverse('vote')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_sign_up(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class ModelsTest(TestCase):

    def setUp(self):
        try:
            from populate_dogs import populate
            populate()
        except ImportError:
            print("Populate_dogs script does not exist")
        except NameError:
            print("Function does not exist")
        except:
            print("Error in function")


    def get_name(self, name):
        from bestboy.models import Dog
        try:
            name = Dog.objects.get_or_create(name=name)
        except Dog.DoesNotExist:
            name = None
        return name

    def get_breed(self, name):
        from bestboy.models import Dog
        try:
            breed = Dog.objects.get_or_create(name=name)
        except Dog.DoesNotExist:
            breed = None
        return breed

    def get_user(self, name):
        from bestboy.models import Test_User
        try:
            username = Test_User.objects.get_or_create(name=name)
        except Test_User.DoesNotExist:
            username = None
        return username

    def test_add_name(self):
        name = self.get_name("Leo")
        self.assertIsNotNone(name)

    def test_add_breed(self):
        breed = self.get_breed("DM")
        self.assertIsNotNone(breed)

    def test_add_username(self):
        username = self.get_user("DundeeBurnsWomen")
        self.assertIsNotNone(username)

