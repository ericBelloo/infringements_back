
# Rest Framework
from rest_framework import serializers
# Models
from apps.infringement.models import (Infringements, InfringementAddress, FractionInfringements, Status)
from apps.vehicle.models import Vehicles
# Serializers
from apps.vehicle.serializers import VehicleSerializer


class InfringementAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfringementAddress
        fields = ('street', 'street_a', 'street_b', 'colony', 'postcode')


class InfringementFractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FractionInfringements
        fields = ('fraction',)

    def create(self, validated_data):
        infringement = validated_data.get('infringement')
        return FractionInfringements.objects.create(**validated_data, infringement=infringement)


class InfringementSerializer(serializers.ModelSerializer):

    folio = serializers.CharField(max_length=20, required=True, allow_null=False, allow_blank=False)
    date = serializers.DateField(required=True, allow_null=False)
    time = serializers.TimeField(required=True, allow_null=False)
    is_absent = serializers.BooleanField(required=True, allow_null=False)
    address = InfringementAddressSerializer(many=False, required=True, allow_null=False)
    vehicle = VehicleSerializer(many=False, required=True, allow_null=False)

    class Meta:
        model = Infringements
        fields = ('folio', 'date', 'time', 'is_absent', 'address', 'vehicle')

    def create(self, validated_data):
        status = Status.objects.get(pk=1)
        address_data = validated_data.pop('address')
        address = InfringementAddress.objects.create(**address_data)
        vehicle_data = validated_data.pop('vehicle')
        vehicle = Vehicles.objects.create(**vehicle_data)
        return self.Meta.model.objects.create(**validated_data, status=status, address=address, vehicle=vehicle)
