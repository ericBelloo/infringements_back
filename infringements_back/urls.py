"""infringements_back URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django urls
    path('admin/', admin.site.urls),
    # My urls
    path('address/', include('apps.address.urls')),
    path('infringement/', include('apps.infringement.urls')),
    path('town-hall/', include('apps.town_hall.urls')),
    path('vehicle/', include('apps.vehicle.urls')),
]
