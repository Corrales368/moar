from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class MyLoginView(LoginView):
    template_name = "authentication/login/login.html"


class MyLogoutView(LogoutView):
    template_name = ""
