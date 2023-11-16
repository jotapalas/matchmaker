import factory
from factory.fuzzy import FuzzyChoice
from core.models import Game

GAME_CHOICES = [
    'Age of Empires II',
    'Age of Empires IV',
    'Europa Universalis IV',
    'Hearts of Iron IV',
    'Stellaris',
    'Victoria 3',
    'Civilization VI',
]


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game
        django_get_or_create = ['name']

    name = FuzzyChoice(GAME_CHOICES)
