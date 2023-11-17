from rest_framework.test import APITestCase
from rest_framework import status
from users.factories import UserFactory
from core.factories import MatchFactory
from core.models import Contender
from django.urls import reverse
from uuid import uuid4


class JoinMatchViewTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.match = MatchFactory()
        self.client.credentials(HTTP_AUTHORIZATION=self.user.get_token())
        self.url = reverse('join-match')
        
    def test_join_match_view(self):
        # First of all, ensure that user is not already in match
        queryset = Contender.objects.filter(user=self.user, match=self.match)
        queryset.delete()

        body = {
            'match_id': self.match.id
        }
        response = self.client.post(self.url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(queryset.exists())
        self.assertEqual(response.data.get('match_id'), str(self.match.id))
        self.assertEqual(response.data.get('user_id'), str(self.user.id))

    def test_join_match_view_bad_request(self):
        body = {
            'foo': 'bar'
        }
        response = self.client.post(self.url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_join_match_view_bad_id_format(self):
        body = {
            'match_id': 'bar'
        }
        response = self.client.post(self.url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_join_match_view_match_not_found(self):
        body = {
            'match_id': uuid4()
        }
        response = self.client.post(self.url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_join_match_view_user_already_in_match(self):
        self.match.add_contender(self.user)
        body = {
            'match_id': self.match.id
        }
        response = self.client.post(self.url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
