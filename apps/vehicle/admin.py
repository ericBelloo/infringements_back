from django.contrib import admin

# Models
from apps.vehicle.models import Colors, Brands, Models


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    pass


@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    pass
