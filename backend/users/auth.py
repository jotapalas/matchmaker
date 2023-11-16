from users.models import User
from uuid import UUID

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
