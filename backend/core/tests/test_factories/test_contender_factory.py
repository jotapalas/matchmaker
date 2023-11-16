from django.test import TestCase
from core.models import Contender
from core.factories import ContenderFactory


class ContenderFactoryTestCase(TestCase):
    def test_contender_factory(self):
        before_count = Contender.objects.count()
        contender = ContenderFactory()
        self.assertEqual(
            Contender.objects.count(),
            before_count + 1,
            'One contender object should have been created'
        )
        self.assertIsNotNone(
            contender.user,
            'Created contender has no user'
        )
        self.assertIsNotNone(
            contender.match,
            'Created contender has no match assigned'
        )
