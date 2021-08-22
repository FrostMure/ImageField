from django.urls import path
from . import views

urlpatterns = [
    path('', views.MostrarImagen),
#    path('photo/', views.MostrarImagen)
]