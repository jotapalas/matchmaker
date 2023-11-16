from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=128, required=True
    )
    password = serializers.CharField(
        max_length=128, required=True
    )

    def authenticate(self) -> User:
        self.is_valid(raise_exception=True)
        return authenticate(**self.validated_data)
