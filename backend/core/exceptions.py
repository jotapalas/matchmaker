from django.utils.translation import gettext_lazy as _


class UserAlreadyInMatch(Exception):
    def __init__(self, user, match, message=None):
        self.user = user
        self.match = match
        self.message = message
        if not self.message:
            self.message = _(f'User {user} is already in match {match}')
        super().__init__(self.message)
        