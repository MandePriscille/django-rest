from django.urls import path
from . import views
from .views import DetailApiView, CreateApiView, UpdateApiView

urlpatterns = [
    path('product/', views.api_view, name='api_view'),
    path('detail/<int:pk>/',DetailApiView.as_view(), name="detail_product" ),
    path('create/', CreateApiView.as_view()),
    path('update/<int:pk>/', UpdateApiView.as_view()),


]