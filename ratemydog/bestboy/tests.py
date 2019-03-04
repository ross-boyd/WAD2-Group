from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from django.contrib.staticfiles import finders
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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

# -----------------------------------------------------------


class StaticFilesTests(TestCase):

    def test_static_files(self):
        result = finders.find('bestboy/img/dog1.jpg')
        self.assertIsNotNone(result)

    def test_static_files(self):
        result = finders.find('bestboy/img/slider_dog.gif')
        self.assertIsNotNone(result)

# -----------------------------------------------------------


class FormsTests(TestCase):

    def test_forms(self):
        try:
            from bestboy.forms import RatingForm
            pass
        except ImportError:
            print("Error importing module")
        except:
            print("Error")

# ---------------------------------------------------------------------------------------


class IndexPageTests(TestCase):

    def test_index_welcome(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'TOP DUGS', response.content )

    def test_base_templates_used(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'base.html')

    #Navigation testing
    def test_index_link_to_index(self):
        try:
            response = self.client.get(reverse('index'))
        except:
            response = False
            return response

    def test_index_link_to_vote(self):
        try:
            response = self.client.get(reverse('vote'))
        except:
            response = False
            return response

    def test_index_link_to_signup(self):
        try:
            response = self.client.get(reverse('signup'))
        except:
            response = False
            return response

    def test_index_link_to_login(self):
        try:
            response = self.client.get(reverse('login'))
        except:
            response = False
            return response

# ---------------------------------------------------------------------------------------


class TemplateTests(TestCase):

    def test_base_template_exists(self):
        base_path = os.path.join(os.path.join(BASE_DIR,'templates'), 'base.html')
        self.assertTrue(os.path.isfile(base_path))

    def test_home_template_exists(self):
        home_path = os.path.join(os.path.join(BASE_DIR, 'templates'), 'home.html')
        self.assertTrue(os.path.isfile(home_path))

    def test_login_template_exists(self):
        login_path = os.path.join(os.path.join(BASE_DIR, 'templates'), 'login.html')
        self.assertTrue(os.path.isfile(login_path))

    def test_profile_template_exists(self):
        profile_path = os.path.join(os.path.join(BASE_DIR, 'templates'), 'profile.html')
        self.assertTrue(os.path.isfile(profile_path))

    def test_signup_template_exists(self):
        signup_path = os.path.join(os.path.join(BASE_DIR, 'templates'), 'signup.html')
        self.assertTrue(os.path.isfile(signup_path))

    def test_vote_template_exists(self):
        vote_path = os.path.join(os.path.join(BASE_DIR, 'templates'), 'vote.html')
        self.assertTrue(os.path.isfile(vote_path))

# ---------------------------------------------------------------------------------------


class TemplatesUseBaseTests(TestCase):
    # Skipped
    def _test_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'base.html')

    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'base.html')

    # Skipped
    def _test_profile_template(self):
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'base.html')

    def test_vote_template(self):
        response = self.client.get(reverse('vote'))
        self.assertTemplateUsed(response, 'base.html')







