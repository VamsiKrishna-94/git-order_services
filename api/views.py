from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        frontend_data = request.data

        serializer = UserSerializer(data=frontend_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        frontend_data = request.data
        username = frontend_data['username']
        password = frontend_data['password']
        user = User.objects.filter(username=username).first()
        if user:
            if user.check_password(password):
                refresh_token = RefreshToken.for_user(user)
                access_token = refresh_token.access_token
                resp = {
                    'refresh_token': str(refresh_token),
                    'access_token': str(access_token),
                  }
                return Response(data=resp, status=status.HTTP_200_OK)
            else:
                return Response(data='Invalid Password', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data='Invalid Username', status=status.HTTP_400_BAD_REQUEST)


class TestView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        history = [
            {
                'date': '3/29/2024',
                'amount': 450
            },
            {
                'date': '3/28/2024',
                'amount': 500
            }
        ]
        return Response(data=history, status=status.HTTP_200_OK)
