# Django
from django.urls import path
# Views
from apps.infringement.views import InfringementLogin

app_name = 'infringement'

urlpatterns = [
    # views
    path('login/', InfringementLogin.as_view(), name='login')
]
