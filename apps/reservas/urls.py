from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [    
    path('lugares/', views.lugaresPage, name='lugares'),
    path('contact/', views.contactPage, name='contact'),
    path('reservas/', views.reservasPage, name='reservar'),
    path('misReservas/', views.misReservasPage, name='misReservas'),
]