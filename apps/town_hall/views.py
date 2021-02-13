# Django
from django.db import transaction
# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Serializers
from apps.town_hall.serializers import UserSerializer, TownHallPersonSerializer
# Models
from django.contrib.auth.models import User


class TownHallPersonView(APIView):

    @transaction.atomic
    def post(self, request):
        if User.objects.filter(username=request.data.get('username')).exists():
            return Response({
                'message': 'User already exists',
            }, status=status.HTTP_400_BAD_REQUEST)
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            town_hall_person_serializer = TownHallPersonSerializer(data=request.data)
            if town_hall_person_serializer.is_valid():
                town_hall_person_serializer.save(user=user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'detail': town_hall_person_serializer.errors,
                }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message': user_serializer.errors.values(),
            }, status=status.HTTP_201_CREATED)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        }, status=status.HTTP_200_OK)

