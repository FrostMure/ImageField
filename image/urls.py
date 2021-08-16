from django.urls import path
from . import views

urlpatterns = [
    path('MostrarImagen/', views.MostrarImagen),
#    path('photo/', views.MostrarImagen)
]