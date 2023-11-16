import factory
from core.models import Contender
from users.factories import UserFactory
from .match_factory import MatchFactory


class ContenderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contender

    user = factory.SubFactory(UserFactory)
    match = factory.SubFactory(MatchFactory)
