from django.contrib import admin
# Models
from apps.infringement.models import Status, InfringementAddress, Infringements, Articles, Fractions


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(InfringementAddress)
class InfringementAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Infringements)
class InfringementsAdmin(admin.ModelAdmin):
    pass


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    pass


@admin.register(Fractions)
class FractionsAdmin(admin.ModelAdmin):
    pass


