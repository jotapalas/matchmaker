from rest_framework import serializers
from users.models import User
from core.models import Match


class ContenderSerializerIn(serializers.Serializer):
    user_id = serializers.UUIDField(
        required=True
    )
    match_id = serializers.UUIDField(
        required=True
    )

    def create(self, validated_data):
        user = User.objects.get(id=validated_data['user_id'])
        match = Match.objects.get(id=validated_data['match_id'])

        return match.add_contender(user)
