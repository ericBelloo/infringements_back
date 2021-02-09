from django.db import models
from django.contrib.auth.models import User


class Persons(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    police_number = models.CharField(max_length=6, null=False, blank=False)
