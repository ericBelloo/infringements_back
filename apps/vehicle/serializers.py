
from rest_framework import serializers
# Models
from apps.vehicle.models import Vehicles


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = ('year', 'plate', 'color', 'model')
