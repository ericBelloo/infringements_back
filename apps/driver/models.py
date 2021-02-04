# Models
from django.db import models
from apps.address.models import States, Postcodes
# Mixins
from helpers.mixins import BaseNameModel


class ClassType(BaseNameModel):
    pass


class License(models.Model):
    number = models.CharField(max_length=12)
    # Foreign Key
    class_type = models.ForeignKey(ClassType, null=True, blank=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(States, null=True, blank=True, on_delete=models.SET_NULL)


class Address(models.Model):
    street = models.CharField(max_length=50, null=True, blank=True)
    street_a = models.CharField(max_length=50, null=True, blank=True)
    street_b = models.CharField(max_length=50, null=True, blank=True)
    # Foreign Key
    postcode = models.ForeignKey(Postcodes, null=True, blank=True, on_delete=models.SET_NULL)


class Drivers(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    paternal = models.CharField(max_length=50, null=True, blank=True)
    maternal = models.CharField(max_length=50, null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True)
    # Foreign Key
    driver_address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
