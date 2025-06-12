from django.urls import path
from . import views

urlpatterns = [
    path('api/otimizar/', views.otimizar_view),
]
