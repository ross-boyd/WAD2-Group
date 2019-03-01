from django.test import TestCase

from django.urls import reverse


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

