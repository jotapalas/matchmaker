from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from users.serializers import LoginSerializer


class LoginView(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            user = serializer.authenticate()

            if user:
                response = Response({
                    'token': user.get_token()
                }, status=status.HTTP_200_OK)
            else:
                response = Response(
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
        except ValidationError as e:
            response = Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response = Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
