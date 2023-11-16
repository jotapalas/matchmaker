from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from .mixins import UUIDMixin
from .match import Match
from .playable import Playable

User = settings.AUTH_USER_MODEL


class Contender(UUIDMixin):
    """
    Every player in a match
    """
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        help_text=_('Match played by the contender'),
        related_name='contenders'
    )
    user = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        help_text=_('User playing this match. If null, it means that user was deleted'),
        related_name='matches'
    )
    playable = models.ForeignKey(
        Playable,
        null=True, blank=True,
        on_delete=models.PROTECT,
        help_text=_('Playable used by the contender at the match')
    )
    is_winner = models.BooleanField(
        default=False,
        help_text=_('This contender won the match')
    )

    def mark_as_winner(self):
        self.is_winner = True
        self.save()
        return self

    def mark_as_loser(self):
        self.is_winner = False
        self.save()
        return self

    class Meta:
        verbose_name = _('contender')
        verbose_name_plural = _('contenders')
        ordering = ['match']
