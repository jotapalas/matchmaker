from django.test import TestCase
from core.models import Game
from core.factories import GameFactory


class GameFactoryTestCase(TestCase):
    def test_game_creation(self):
        before_count = Game.objects.count()
        GameFactory()
        self.assertEqual(
            Game.objects.count(),
            before_count + 1,
            'One game should have been created'
        )
        