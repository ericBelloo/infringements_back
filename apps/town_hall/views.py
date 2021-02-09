# Django
from django.db import transaction
# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# Serializers
from apps.town_hall.serializers import UserSerializer, TownHallPersonSerializer


class TownHallPersonView(APIView):

    @transaction.atomic
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            town_hall_person_serializer = TownHallPersonSerializer(data=request.data)
            if town_hall_person_serializer.is_valid():
                town_hall_person_serializer.save(user=user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'token': None,
                    'error': town_hall_person_serializer.errors.values(),
                }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'token': None,
                'error': user_serializer.errors,
            }, status=status.HTTP_201_CREATED)





