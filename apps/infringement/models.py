# Models
from django.db import models
from apps.address.models import Postcodes
from apps.driver.models import Drivers
# Mixins
from apps.vehicle.models import Vehicles
from helpers.mixins import BaseNameModel


class Status(BaseNameModel):
    pass


class InfringementAddress(models.Model):
    street = models.CharField(max_length=50, null=True, blank=True, verbose_name='infringement_street')
    street_a = models.CharField(max_length=50, null=True, blank=True, verbose_name='infringement_street_a')
    street_b = models.CharField(max_length=50, null=True, blank=True,  verbose_name='infringement_street_b')
    # Foreign Key
    postcode = models.ForeignKey(Postcodes, null=True, blank=True, on_delete=models.SET_NULL)


class Infringements(models.Model):
    folio = models.CharField(max_length=6, null=False, blank=False, unique=True)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    is_paid = models.BooleanField(default=False)
    is_absent = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    # Foreign Keys
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.ForeignKey(InfringementAddress, null=True, blank=True, on_delete=models.SET_NULL)
    vehicle = models.ForeignKey(Vehicles, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-date', '-time']


class Articles(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)


class Fractions(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    uma = models.SmallIntegerField()
    # Foreign Key
    article = models.ForeignKey(Articles, null=True, blank=True, on_delete=models.SET_NULL)


class FractionInfringements(models.Model):
    # Foreign Key
    fraction = models.ForeignKey(Fractions, null=True, blank=True, on_delete=models.SET_NULL)
    infringement = models.ForeignKey(Infringements, null=True, blank=True, on_delete=models.SET_NULL)


class Payments(models.Model):
    date = models.DateField(null=False, blank=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    surcharges = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)  # recargos
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    # Foreign Key
    infringement = models.ForeignKey(Infringements, null=True, blank=True, on_delete=models.SET_NULL)
