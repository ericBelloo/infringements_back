from django.db import models

# Mixins
from helpers.mixins import BaseNameModel


class Colors(BaseNameModel):
    pass


class Brands(BaseNameModel):
    pass


class Models(BaseNameModel):
    # Foreign Keys
    brand = models.ForeignKey(Brands, null=True, blank=False, on_delete=models.SET_NULL)


class Vehicles(models.Model):
    year = models.SmallIntegerField()
    plate = models.CharField(max_length=10, null=True, blank=True)  # placa
    # Foreign Key
    color = models.ForeignKey(Colors, null=True, blank=True, on_delete=models.SET_NULL)
    model = models.ForeignKey(Models, null=True, blank=True, on_delete=models.SET_NULL)





