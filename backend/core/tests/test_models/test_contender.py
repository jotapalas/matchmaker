from django.test import TestCase
from core.models import Contender
from core.factories import ContenderFactory


class ContenderTestCase(TestCase):
    def setUp(self):
        self.contender = ContenderFactory()

    def test_mark_as_winner(self):
        self.contender.mark_as_winner()
        self.assertTrue(self.contender.is_winner)

    def test_mark_as_loser(self):
        self.contender.mark_as_loser()
        self.assertFalse(self.contender.is_winner)
