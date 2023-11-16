from django.test import TestCase
from users.factories import UserFactory
from users.serializers import LoginSerializer


class TestLoginSerializer(TestCase):
    def setUp(self):
        self.body = {
            'username': 'user',
            'password': 'password'
        }
        self.user = UserFactory(**self.body)

    def test_login_serializer(self):
        serializer = LoginSerializer(data=self.body)
        user = serializer.authenticate()
        self.assertEqual(user, self.user)

    def test_bad_login_serializer(self):
        serializer = LoginSerializer(data={
            'username': 'non_existing',
            'password': 'bad_password'
        })
        user = serializer.authenticate()
        self.assertIsNone(user)
