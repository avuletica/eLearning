from django.test import TestCase, RequestFactory
from django.contrib.auth.hashers import make_password

from .models import UserProfile
from courses.views import courses


class UserProfileTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = UserProfile.objects.create_user(
            username='Hodor', email='test@gmail.com', password='top_secret')

    def test_user_can_register(self):
        UserProfile.objects.create(username="user_name_sample", email='t@t.com', password=make_password('abcd'))
        user = UserProfile.objects.get(username="user_name_sample")
        self.assertEqual(user.username, 'user_name_sample')

    def test_user_can_login(self):
        request = self.factory.get('courses')
        request.user = self.user
        response = courses(request)
        self.assertEqual(response.status_code, 200)

    def test_call_view_denies_anonymous(self):
        response = self.client.get('profile', follow=True)
        self.assertEqual(response.status_code, 404)
        response = self.client.get('courses', follow=True)
        self.assertEqual(response.status_code, 404)
