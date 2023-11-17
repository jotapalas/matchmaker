from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import status
from core.models import Match
from core.serializers import (
    ContenderSerializerIn,
    ContenderSerializerOut,
)
from core.exceptions import UserAlreadyInMatch
from users.auth import CustomTokenAuthentication



class JoinMatchView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomTokenAuthentication]

    def post(self, request):
        match_id = request.data.get('match_id')
        user_id = request.user.id
        data = dict(
            user_id=user_id,
            match_id=match_id
        )
        try:
            serializer = ContenderSerializerIn(data=data)
            serializer.is_valid(raise_exception=True)
            contender = serializer.save()

            response = Response(
                ContenderSerializerOut(contender).data,
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            response = Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except UserAlreadyInMatch as e:
            response = Response(
                {'error': str(e)},
                status=status.HTTP_403_FORBIDDEN
            )
        except Match.DoesNotExist:
            response = Response(
                {'error': f'Match with id {match_id} was not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        return response
