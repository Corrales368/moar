from unicodedata import name
from django.urls import path
from django.conf.urls import url
from . import views

app_name = "authentication"

urlpatterns = [    
    path('', views.loginUser, name='login'),
]