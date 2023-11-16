from django.test import TestCase
from users.factories import UserFactory
from users.auth import get_user_from_token
from django.utils.crypto import get_random_string


class TestAuth(TestCase):
    def test_get_user_from_token(self):
        user = UserFactory()
        token = user.get_token()
        authenticated_user = get_user_from_token(token)
        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user, user)

    def test_bad_token(self):
        bad_token = get_random_string(length=32)
        authenticated_user = get_user_from_token(bad_token)
        self.assertIsNone(authenticated_user)
