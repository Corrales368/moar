from django.urls import path
from . import views

app_name = "user"

urlpatterns = [    
    path('', views.register, name='register'),
    path('register/', views.register, name='register'),
] 

