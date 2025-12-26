from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_view, name='api_view'),
    path('auth/', obtain_auth_token),
]