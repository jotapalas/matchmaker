from django.test import TestCase
from core.models import Playable
from core.factories import PlayableFactory


class PlayableFactoryTestCase(TestCase):
    def test_playable_factory(self):
        before_count = Playable.objects.count()
        PlayableFactory()
        self.assertEqual(
            Playable.objects.count(),
            before_count + 1,
            'One playable object should have been created'
        )
