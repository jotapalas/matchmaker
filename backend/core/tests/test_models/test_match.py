from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from users.factories import UserFactory
from core.factories import MatchFactory
from core.exceptions import UserAlreadyInMatch


class MatchTestCase(TestCase):
    def setUp(self):
        self.match = MatchFactory()

    def test_wrong_dates(self):
        now = timezone.now()
        yesterday = now - timedelta(days=1)
        self.match.datetime_start = now
        self.match.datetime_end = yesterday
        self.assertRaises(
            ValidationError,
            self.match.save,
            'Match model should prevent wrong dates to be saved'
        )

    def test_start_match(self):
        self.match.start_match()
        self.assertTrue(self.match.is_started)

    def test_end_match(self):
        self.match.end_match()
        self.assertTrue(self.match.is_ended)

    def test_add_contender(self):
        user = UserFactory()
        before_count = self.match.contenders.count()
        self.match.add_contender(user)
        self.assertEqual(
            self.match.contenders.count(),
            before_count + 1,
            'Contender was not added to match'
        )
        self.assertTrue(
            self.match.contenders.filter(user=user).exists(),
            'Contender was not added correctly'
        )

    def test_add_contender_twice(self):
        user = UserFactory()
        self.match.add_contender(user)
        self.assertRaises(
            UserAlreadyInMatch,
            self.match.add_contender,
            user
        )
