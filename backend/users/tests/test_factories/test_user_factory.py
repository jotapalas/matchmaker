from django.test import TestCase
from users.factories import UserFactory
from users.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate


class TestUserFactory(TestCase):
    def test_user_factory(self):
        before_count = User.objects.count()
        UserFactory()
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count + 1)

    def test_user_factory_with_password(self):
        username = get_random_string(length=8)
        password = get_random_string(length=8)
        kwargs = {
            'username': username,
            'password': password
        }
        user = UserFactory(**kwargs)
        authenticated_user = authenticate(**kwargs)
        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user, user)
