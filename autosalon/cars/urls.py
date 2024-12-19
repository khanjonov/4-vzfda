from django.urls import path
from . import views

urlpatterns = [
    path('', views.brand_list, name='brand_list'),
    path('cars/', views.car_list, name='car_list'),
]
