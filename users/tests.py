from django.test import TestCase, RequestFactory
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.test import Client

from .models import UserProfile


class UserProfileTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = UserProfile.objects.create_user(
            username='Hodor', email='test@gmail.com', password='top_secret', is_active=True)

    def test_user_can_register(self):
        UserProfile.objects.create(username="user_name_sample", email='t@t.com', password=make_password('abcd'))
        user = UserProfile.objects.get(username="user_name_sample")
        self.assertEqual(user.username, 'user_name_sample')

    def test_user_can_login(self):
        self.c = Client()
        self.user = authenticate(username='Hodor', password='top_secret')
        login = self.c.login(username='Hodor', password='top_secret')
        self.assertTrue(login)

    def test_call_view_denies_anonymous(self):
        response = self.client.get('profile', follow=True)
        self.assertEqual(response.status_code, 404)
        response = self.client.get('courses', follow=True)
        self.assertEqual(response.status_code, 404)
