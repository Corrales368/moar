from django.urls import path
from . import views


app_name = "authentication"

urlpatterns = [
    path('login', views.MyLoginView.as_view(), name="login"),
    path('logout', views.MyLogoutView.as_view(), name="logout")
]
