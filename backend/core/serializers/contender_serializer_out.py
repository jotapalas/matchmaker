from rest_framework import serializers
from users.models import User
from core.models import Match


class ContenderSerializerOut(serializers.Serializer):
    user_id = serializers.UUIDField(
        read_only=True
    )
    match_id = serializers.UUIDField(
        read_only=True
    )
    playable_id = serializers.UUIDField(
        read_only=True
    )
