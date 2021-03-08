
# Django
from django.db import transaction
# Rest Framework
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Serializers
from apps.infringement.serializers import (InfringementSerializer, InfringementFractionSerializer)
from apps.driver.serializers import DriverSerializer
# Utils
from helpers.enums import InfringementEnum
from apps.infringement.utils import get_value


class InfringementLogin(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'username': request.user.username,
            'fist_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        return Response(content, status=status.HTTP_200_OK)


class InfringementView(APIView):

    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        infringement_serializer = InfringementSerializer(data=request.data)
        if infringement_serializer.is_valid(raise_exception=True):
            infringement = infringement_serializer.save()
        else:
            infringement = None

        fractions = request.data.get('fractions')
        amount = 0
        for item in fractions:
            amount += (item['uma'] * InfringementEnum.UMA_RATE.value)
            fraction_serializer = InfringementFractionSerializer(data=item)
            if fraction_serializer.is_valid(raise_exception=True):
                fraction_serializer.save(infringement=infringement)
        infringement.amount = amount
        if not bool(request.data.get('is_absent')):
            driver = request.data.get('driver')
            driver_data = {
                'name': driver.get('name'),
                'paternal': driver.get('paternal'),
                'maternal': driver.get('maternal'),
                'gender': driver.get('gender'),
                'driver_address': get_value(driver.get('driver_address'))
            }
            driver_serializer = DriverSerializer(data=driver_data)
            if driver_serializer.is_valid(raise_exception=True):
                infringement.driver = driver_serializer.save()
        infringement.save()
        return Response(
            {'message': 'Ok'},
            status=status.HTTP_201_CREATED
        )
