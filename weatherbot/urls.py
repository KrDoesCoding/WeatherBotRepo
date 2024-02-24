from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.weather_report, name='weather_report'),
]

