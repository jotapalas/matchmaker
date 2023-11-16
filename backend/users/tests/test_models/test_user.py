from django.test import TestCase
from users.factories import UserFactory
from users.auth import get_user_from_token


class TestUser(TestCase):
    def test_create_token(self):
        user = UserFactory()
        token = user.get_token()
        self.assertIsNotNone(token)
