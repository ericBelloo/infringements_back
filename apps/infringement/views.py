
# Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Models
from django.contrib.auth.models import User
from apps.town_hall.models import Persons


class InfringementLogin(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'username': request.user.username,
            'fist_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        return Response(content)



