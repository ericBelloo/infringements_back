
from django.db import models

# Create your models here.
from helpers.mixins import BaseNameModel


class States(BaseNameModel):
    pass


class Cities(BaseNameModel):
    # Foreign Key
    state = models.ForeignKey(States, null=True, blank=True, on_delete=models.SET_NULL)


class Colonies(BaseNameModel):
    # Foreign Key
    city = models.ForeignKey(Cities, null=True, blank=True, on_delete=models.SET_NULL)


class Postcodes(BaseNameModel):
    postcode = models.CharField(primary_key=True, blank=False, null=False)

    # Foreign Key
    colony = models.ForeignKey(Colonies, blank=True, null=False, on_delete=models.SET_NULL)
