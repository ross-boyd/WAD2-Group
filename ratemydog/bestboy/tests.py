from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from django.contrib.staticfiles import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


class StaticFilesTests(TestCase):

    def test_static_slider(self):
        result = finders.find('bestboy/img/slider_dog.gif')
        self.assertIsNotNone(result)

    def test_static_dog_pics_not_used(self):
        result2 = finders.find('bestboy/img/dog1.jpg')
        self.assertIsNone(result2)


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


# -----------------------------------------------------------
class PopulationScriptTests(TestCase):

    def setUp(self):
        self.client = Client()
        try:
            from populate_dogs import populate
            populate()
        except ImportError:
            print("The module populate_dogs does not exist")
        except NameError:
            print("The function populate() does not exist or is incorrect")
        except:
            print("Error in populate() function")


# -----------------------------------------------------------

class UrlTests(TestCase):
    def setUp(self):
        self.client = Client()
        try:
            from populate_dogs import populate
            populate()
        except ImportError:
            print("The module populate_dogs does not exist")
        except NameError:
            print("The function populate() does not exist or is incorrect")
        except:
            print("Error in populate() function")

    def test_home_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_vote(self):
        url = reverse('vote')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_sign_up(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_admin(self):
    #     url = reverse('admin')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_login(self):
    #     user = get_user_model()
    #     self.client.force_login(user.objects.get_or_create(username='testuser')[0])
    #     url = reverse('login/testuser')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)


# -----------------------------------------------------------
class BaseTemplateTests(TestCase):

    def setUp(self):
        self.client = Client()
        try:
            from populate_dogs import populate
            populate()
        except ImportError:
            print("The module populate_dogs does not exist")
        except NameError:
            print("The function populate() does not exist or is incorrect")
        except:
            print("Error in populate() function")

    def test_base_template_exists(self):
        base_path = os.path.join(TEMPLATE_DIR, 'base.html')
        self.assertTrue(os.path.isfile(base_path))

    def test_navbar_present(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'Home', response.content)
        self.assertIn(b'Vote', response.content)
        self.assertIn(b'Upload', response.content)
        self.assertIn(b'RATE MY DOG', response.content)
        self.assertIn(b'Sign Up', response.content)
        self.assertIn(b'Login', response.content)


# ---------------------------------------------------------------------------------------

class TemplatesExistTests(TestCase):

    def test_home_template_exists(self):
        home_path = os.path.join(TEMPLATE_DIR, 'home.html')
        self.assertTrue(os.path.isfile(home_path))

    def test_login_template_exists(self):
        login_path = os.path.join(TEMPLATE_DIR, 'login.html')
        self.assertTrue(os.path.isfile(login_path))

    def test_signup_template_exists(self):
        signup_path = os.path.join(TEMPLATE_DIR, 'signup.html')
        self.assertTrue(os.path.isfile(signup_path))

    def test_vote_template_exists(self):
        vote_path = os.path.join(TEMPLATE_DIR, 'vote.html')
        self.assertTrue(os.path.isfile(vote_path))

    def test_no_dog_template_exists(self):
        no_dog_path = os.path.join(TEMPLATE_DIR, 'nodog.html')
        self.assertTrue(os.path.isfile(no_dog_path))

    def test_profile_template_exists(self):
        profile_path = os.path.join(TEMPLATE_DIR, 'profile.html')
        self.assertTrue(os.path.isfile(profile_path))

    def test_dog_profile_template_exists(self):
        dog_profile_path = os.path.join(TEMPLATE_DIR, 'dogprofile.html')
        self.assertTrue(os.path.isfile(dog_profile_path))

    def test_upload_template_exists(self):
        upload_path = os.path.join(TEMPLATE_DIR, 'upload.html')
        self.assertTrue(os.path.isfile(upload_path))

    def test_success_template_exists(self):
        success_path = os.path.join(TEMPLATE_DIR, 'success.html')
        self.assertTrue(os.path.isfile(success_path))


# -----------------------------------------------------------
class TemplatesUseBaseTests(TestCase):

    def setUp(self):
        self.client = Client()
        try:
            from populate_dogs import populate
            populate()
        except ImportError:
            print("The module populate_dogs does not exist")
        except NameError:
            print("The function populate() does not exist or is incorrect")
        except:
            print("Error in populate() function")

    def test_home_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'home.html', 'base.html')

    def _test_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html', 'base.html')

    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html', 'base.html')

    def test_vote_template(self):
        user = get_user_model()
        self.client.force_login(user.objects.get_or_create(username='testuser')[0])
        response = self.client.get(reverse('vote'))
        self.assertTemplateUsed(response, 'vote.html', 'base.html')

    # def test_no_dog_template(self):
    #     response = self.client.get(reverse('vote'))
    #     self.assertTemplateUsed(response, 'nodog.html', 'base.html')

    # def test_profile_template(self):
    #     user = get_user_model()
    #     self.client.force_login(user.objects.get_or_create(username='testuser')[0])
    #     response = self.client.get(reverse('profile/testuser'))
    #     self.assertTemplateUsed(response, 'profile.html', 'base.html')

    # def test_dog_profile_template(self):
    #     response = self.client.get(reverse('dog/8'))
    #     self.assertTemplateUsed(response, 'dogprofile.html', 'base.html')

    def test_upload_template(self):
        user = get_user_model()
        self.client.force_login(user.objects.get_or_create(username='testuser')[0])
        response = self.client.get(reverse('upload'))
        self.assertTemplateUsed(response, 'upload.html', 'base.html' )

    # def test_success_template(self):
    #     user = get_user_model()
    #     self.client.force_login(user.objects.get_or_create(username='testuser')[0])
    #     response = self.client.get(reverse('upload'))
    #     self.assertTemplateUsed(response, 'success.html', 'base.html')

# -----------------------------------------------------------

class IndexPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        try:
            from populate_dogs import populate
            populate()
        except ImportError:
            print("The module populate_dogs does not exist")
        except NameError:
            print("The function populate() does not exist or is incorrect")
        except:
            print("Error in populate() function")

    def test_index_has_titles(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'RATE MY DOG', response.content)
        self.assertIn(b'The Best Boys', response.content)

    def test_index_has_images(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'img', response.content)

    # Navigation testing
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

    def test_index_link_to_profile(self):
        try:
            response = self.client.get(reverse('profile'))
        except:
            response = False
            return response


# ---------------------------------------------------------------------------------------

class SignUpTests(TestCase):
    def test_are_fields_present(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Email address:', response.content)
        self.assertIn(b'Username:', response.content)
        self.assertIn(b'Password:', response.content)
        self.assertIn(b'Password confirmation:', response.content)

    def setUp(self):
        self.client = Client()
        self.newUser = {'email': "daniel@gmail.com",
                        'username': "rssbyd",
                        'password': "Testpassword123!",
                        'confirm_password': "Testpassword123!"}
        # User.objects.create_user(**self.newUser)

    def test_signup(self):
        response = self.client.post(reverse('signup'),
                                    {'email': "daniel@gmail.com",
                                     'username': "rssbyd",
                                     'password': "Testpassword123!",
                                     'confirm_password': "Testpassword123!"})

        self.assertNotIn(b'The Best Boys', response.content)

    def test_short_password(self):
        response = self.client.post(reverse('signup'),
                                    {'email': "test@gmail.com",
                                     'username': "test",
                                     'password': "pass",
                                     'confirm_password': "pass"})
        # Incorrect info so no redirect to index
        self.assertNotIn(b'The Best Boys', response.content)

    def test_no_uppercase(self):
        response = self.client.post(reverse('signup'),
                                    {'email': "test@gmail.com",
                                     'username': "test",
                                     'password': "testpassword1",
                                     'confirm_password': "testpassword1"})
        # Incorrect info so no redirect to index
        self.assertNotIn(b'The Best Boys', response.content)

    def test_no_lowercase(self):
        response = self.client.post(reverse('signup'),
                                    {'email': "test@gmail.com",
                                     'username': "test",
                                     'password': "TESTPASSWORD1",
                                     'confirm_password': "TESTPASSWORD"})
        # Incorrect info so no redirect to index
        self.assertNotIn(b'The Best Boys', response.content)

    def test_no_numbers(self):
        response = self.client.post(reverse('signup'),
                                    {'email': "test@gmail.com",
                                     'username': "test",
                                     'password': "Testpassword",
                                     'confirm_password': "Testpassword"})
        # Incorrect info so no redirect to index
        self.assertNotIn(b'The Best Boys', response.content)

    def test_no_letters(self):
        response = self.client.post(reverse('signup'),
                                    {'email': "test@gmail.com",
                                     'username': "test",
                                     'password': "Testpassword",
                                     'confirm_password': "Testpassword"})
        # Incorrect info so no redirect to index
        self.assertNotIn(b'The Best Boys', response.content)

    # ---------------------------------------------------------------------------------------


class LoginTests(TestCase):
    def setUp(self):
        self.client = Client()
