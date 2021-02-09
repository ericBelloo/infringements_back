
from rest_framework.authtoken import views
from django.urls import path
# Views
from apps.infringement.views import InfringementLogin

app_name = 'infringement'

urlpatterns = [
    # views
    path('api-token-auth/', views.obtain_auth_token),
    path('login/', InfringementLogin.as_view(), name='login')
]
