from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reservas:lugares') 
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.") 
            return render(request, 'authentication/login/login.html', {'error_message': messages.get_messages(request)})
    else:
        return render(request, 'authentication/login/login.html')