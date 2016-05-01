from django.test import TestCase, RequestFactory

from users.models import UserProfile
from forum.views import forum


class TestCalls(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = UserProfile.objects.create_user(
            username='Hodor', email='test@gmail.com', password='top_secret')

    def test_call_view_denies_anonymous(self):
        response = self.client.get('forum', follow=True)
        self.assertEqual(response.status_code, 404)

    # Test forum view after login
    def test_call_view_loads(self):
        # Create an instance of a GET request.
        request = self.factory.get('forum')
        request.user = self.user
        response = forum(request)
        self.assertEqual(response.status_code, 200)
