from django.test import TestCase
from core.models import Match, Contender
from core.serializers import ContenderSerializerIn
from core.factories import MatchFactory
from core.exceptions import UserAlreadyInMatch
from users.factories import UserFactory
from users.models import User
from uuid import uuid4


class ContenderSerializerInTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.match = MatchFactory()

    def test_contender_serializer_in(self):
        data = dict(
            user_id=self.user.id,
            match_id=self.match.id
        )
        queryset = Contender.objects.filter(
            user=self.user,
            match=self.match
        )
        before_count = queryset.count()
        serializer = ContenderSerializerIn(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(
            queryset.count(),
            before_count + 1,
            'Contender was not created in the database'
        )

    def test_contender_serializer_in_wrong_input(self):
        data = dict(
            user_id='wrong_id',
            match_id='wrong_id'
        )
        serializer = ContenderSerializerIn(data=data)
        self.assertFalse(serializer.is_valid())

    def test_contender_serializer_in_user_not_found(self):
        data = dict(
            user_id=uuid4(),
            match_id=self.match.id
        )
        serializer = ContenderSerializerIn(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertRaises(User.DoesNotExist, serializer.save)

    def test_contender_serializer_in_match_not_found(self):
        data = dict(
            user_id=self.user.id,
            match_id=uuid4()
        )
        serializer = ContenderSerializerIn(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertRaises(Match.DoesNotExist, serializer.save)

    def test_contender_serializer_in_user_already_in_match(self):
        self.match.add_contender(self.user)
        data = dict(
            user_id=self.user.id,
            match_id=self.match.id
        )
        queryset = Contender.objects.filter(
            user=self.user,
            match=self.match
        )
        before_count = queryset.count()
        serializer = ContenderSerializerIn(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertRaises(UserAlreadyInMatch, serializer.save)
        self.assertEqual(
            queryset.count(),
            before_count,
            'Contender was not created in the database'
        )
