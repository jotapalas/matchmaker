from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth import get_user_model
from .mixins import UUIDMixin
from .game import Game

User = get_user_model()


class Match(UUIDMixin):
    """
    Every match of a particular game
    """
    game = models.ForeignKey(
        Game,
        on_delete=models.PROTECT,
        related_name='matches',
        help_text=_('The game played at this match')
    )
    datetime_start = models.DateTimeField(
        null=True, blank=True,
        help_text=_('Date and time for the match to start')
    )
    datetime_end = models.DateTimeField(
        null=True, blank=True,
        help_text=_('Date and time when the match ended')
    )

    def __str__(self):
        return f'{str(self.game)} ({self.datetime_start})'

    def _validate_start_end_dates(self):
        if (
            self.datetime_start and self.datetime_end
            and self.datetime_start > self.datetime_end
        ):
            raise ValidationError(
                _('End date cannot be before start date.')
            )

    @property
    def is_started(self):
        return self.datetime_start is not None\
            and self.datetime_start <= timezone.now()
    
    @property
    def is_ended(self):
        return self.datetime_end is not None\
            and self.datetime_end <= timezone.now()
    
    @property
    def winners(self):
        return self.contenders.filter(is_winner=True)

    def save(self, *args, **kwargs):
        self._validate_start_end_dates()
        return super().save(*args, **kwargs)
    
    def start_match(self):
        self.datetime_start = timezone.now()
        self.save()

    def end_match(self):
        now = timezone.now()

        if self.datetime_start is None:
            self.datetime_start = now

        self.datetime_end = now
        self.save()
    
    def add_contender(self, user: User):
        from core.models import Contender
        contender, is_new = Contender.objects.get_or_create(
            match=self, user=user
        )
        if not is_new:
            raise ValidationError(
                _('Contender is already in match')
            )

        return contender


    class Meta:
        verbose_name = _('match')
        verbose_name_plural = _('matches')
        ordering = ['game', '-datetime_start']
