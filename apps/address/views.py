# Django
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
# Models
from apps.address.models import Postcodes, Cities, Colonies


class Colony(object):
    pass


class AddressView(APIView):

    def get(self, request):
        postcodes = Postcodes.objects.filter(postcode=self.request.GET.get('postcode'))
        colonies = [(postcode.colony.id, postcode.colony.name) for postcode in postcodes]
        first = postcodes.first()
        colony = Colonies.objects.get(pk=first.colony.id)
        data = {
            'colonies': colonies,
            'city': colony.city.name,
            'state': colony.city.state.name
        }
        return Response(data=data, status=status.HTTP_200_OK)


