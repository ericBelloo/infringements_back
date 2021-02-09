# Django
from django.urls import path
# Views
from apps.town_hall.views import TownHallPersonView, CustomAuthToken
# RestFramework
from rest_framework.authtoken import views

app_name = 'town_hall'

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view(), name='custom_auto_token'),  # generate token
    path('create-town-hall-person/', TownHallPersonView.as_view(), name='create_town_hall_person')
]
