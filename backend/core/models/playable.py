from django.db import models
from .mixins import UUIDMixin, DateLoggedMixin
from .game import Game
from django.utils.translation import gettext_lazy as _


class Playable(UUIDMixin, DateLoggedMixin):
    """
    Any playable nation / faction / hero / anything the player will use while playing a match.
    For example: In AoE2, player can play with Aztecs
    """
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='playables',
        help_text=_('The game to which this playable belongs')
    )
    name = models.CharField(
        null=False, blank=False,
        max_length=128,
        help_text=_('Name of the game. Unique. Ex: Age of Empires II.'),
        unique=True,
        db_index=True
    )

    def __str__(self):
        return f'{self.name} ({str(self.game)})'

    class Meta:
        verbose_name = _('playable')
        verbose_name_plural = _('playables')
        ordering=['game', 'name']
