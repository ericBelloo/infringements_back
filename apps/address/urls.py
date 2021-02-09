
from django.urls import path
# utils
from apps.address.utils import process_postcodes
from apps.address.views import AddressView

app_name = 'address'

urlpatterns = [
    # views
    path('get-address/', AddressView.as_view(), name='get_address'),
    # catalogs
    path('process-postcodes/', process_postcodes, name='process_postcodes'),
]
