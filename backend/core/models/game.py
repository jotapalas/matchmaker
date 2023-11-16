from django.utils.translation import gettext_lazy as _
from django.db import models
from .mixins import (UUIDMixin, DateLoggedMixin)


class Game(UUIDMixin, DateLoggedMixin):
    """
    Any game that could be played by the players.
    """
    name = models.CharField(
        null=False, blank=False,
        max_length=128,
        help_text=_('Name of the game. Unique. Ex: Age of Empires II.'),
        unique=True,
        db_index=True
    )

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = _('game')
        verbose_name_plural = _('games')
        ordering = ['name']
