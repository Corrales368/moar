from django.shortcuts import render
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'authentication/login/login.html'

# Create your views here.
def loginUser(request):
    return render(request, 'authentication/login/login.html')
