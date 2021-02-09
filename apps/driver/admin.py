from django.contrib import admin
# Models
from apps.driver.models import Drivers, DriverAddress, License, ClassType


@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverAddress)
class DriverAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassType)
class ClassType(admin.ModelAdmin):
    pass
