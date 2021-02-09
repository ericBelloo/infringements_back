
# Rest Framework
from rest_framework import serializers
# Models
from django.contrib.auth.models import User
from apps.town_hall.models import Persons


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=191, allow_null=False)
    first_name = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    password = serializers.CharField(max_length=50, allow_null=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


class TownHallPersonSerializer(serializers.ModelSerializer):
    police_number = serializers.CharField(max_length=6, allow_null=False, allow_blank=False)

    class Meta:
        model = Persons
        fields = ('police_number',)

    def create(self, validated_data):
        return Persons.objects.create(**validated_data)
