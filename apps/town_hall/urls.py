
from django.urls import path
# Views
from apps.town_hall.views import TownHallPersonView

app_name = 'town_hall'

urlpatterns = [
    path('create-town-hall-person/', TownHallPersonView.as_view(), name='create_town_hall_person')
]
