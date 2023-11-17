from users.models import User
from uuid import UUID
from rest_framework import authentication
from rest_framework import exceptions

def get_user_from_token(token: str) -> User:
    """Receives a token and decodes it to a User object.

    Args:
        token (str): The token identifying the user

    Returns:
        User: The identified user if token is correct, else None
    """
    try:
        uuid = UUID(token)
        user = User.objects.get(id=uuid)
    except (ValueError, User.DoesNotExist):
        user = None

    return user


class CustomTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user_token = request.META.get('HTTP_AUTHORIZATION')

        user = get_user_from_token(user_token)

        if user is None:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        return (user, None) # authentication successful
