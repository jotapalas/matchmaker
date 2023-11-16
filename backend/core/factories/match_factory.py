import factory
from core.models import Match
from .game_factory import GameFactory


class MatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Match

    game = factory.SubFactory(GameFactory)
