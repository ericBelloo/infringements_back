
# Rest Framework
from rest_framework import serializers
# Models
from apps.driver.models import Drivers, DriverAddress


class DriverAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = DriverAddress
        fields = ('street', 'street_a', 'street_b', 'colony', 'postcode')


class DriverSerializer(serializers.ModelSerializer):
    driver = DriverAddressSerializer(many=False, required=False, allow_null=True)

    class Meta:
        model = Drivers
        fields = ('name', 'paternal', 'maternal', 'driver')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = DriverAddress.objects.create(**address_data)
        return Drivers.objects.create(**validated_data, address=address)
