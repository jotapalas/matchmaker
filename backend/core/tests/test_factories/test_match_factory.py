from django.test import TestCase
from core.models import Match
from core.factories import MatchFactory


class MatchFactoryTestCase(TestCase):
    def test_match_factory(self):
        before_count = Match.objects.count()
        MatchFactory()
        self.assertEqual(
            Match.objects.count(),
            before_count + 1,
            'One match object should have been created'
        )
