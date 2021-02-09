from django.contrib import admin
from apps.address.models import States, Cities, Colonies, Postcodes


@admin.register(States)
class StatesAdmin(admin.ModelAdmin):
    pass


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    pass


@admin.register(Colonies)
class ColoniesAdmin(admin.ModelAdmin):
    pass


@admin.register(Postcodes)
class PostCodesAdmin(admin.ModelAdmin):
    pass

