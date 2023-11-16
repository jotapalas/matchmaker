import factory
from factory.fuzzy import FuzzyText
from core.models import Playable
from .game_factory import GameFactory


class PlayableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Playable

    game = factory.SubFactory(GameFactory)
    name = FuzzyText(length=32)
