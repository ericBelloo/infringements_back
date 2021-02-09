
from django.db import models

# Create your models here.
from helpers.mixins import BaseNameModel


class States(BaseNameModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'


class Cities(BaseNameModel):
    # Foreign Key
    state = models.ForeignKey(States, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} - {self.state.name}'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Colonies(BaseNameModel):
    # Foreign Key
    city = models.ForeignKey(Cities, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} - {self.city.name}'

    class Meta:
        verbose_name = 'Colony'
        verbose_name_plural = 'Colonies'


class Postcodes(BaseNameModel):
    postcode = models.CharField(max_length=5, null=True)
    # Foreign Key
    colony = models.ForeignKey(Colonies, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.postcode} - {self.colony.name}'

    class Meta:
        verbose_name = 'Postcode'
        verbose_name_plural = 'Postcodes'
