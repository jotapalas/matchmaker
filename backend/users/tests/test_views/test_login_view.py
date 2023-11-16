from rest_framework.test import APITestCase
from users.factories import UserFactory
from django.urls import reverse
from rest_framework import status
from users.auth import get_user_from_token


class TestLoginView(APITestCase):
    def setUp(self):
        self.body = {
            'username': 'user',
            'password': 'pass1234'
        }
        self.user = UserFactory(**self.body)
        self.url = reverse('users-login')

    def test_login_view(self):
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token')
        self.assertIsNotNone(token)
        user = get_user_from_token(token)
        self.assertEqual(user, self.user)
