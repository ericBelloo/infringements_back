
# Django
from django.urls import path
# Utils
from apps.vehicle.utils import process_vehicle_catalogs, process_vehicle_catalogs_related

app_name = 'vehicle'

urlpatterns = [
    path('process-catalogs/', process_vehicle_catalogs, name='process_catalogs'),
    path('process-catalogs-releted/', process_vehicle_catalogs_related, name='process_catalogs_related'),
]
