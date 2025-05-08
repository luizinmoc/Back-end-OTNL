from django.urls import path
from .views import otimizar

urlpatterns = [
    path('otimizar/', otimizar),
]
