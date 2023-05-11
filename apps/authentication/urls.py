from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [    
    path('', views.RegisterUser, name='login'),
    path('register/', views.RegisterUser, name='register'),
    path('login/', views.loginUser, name='login'),
]