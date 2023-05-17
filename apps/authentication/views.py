from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ..user.models import User
from datetime import datetime
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['usuario']=user.username
            request.session['id']=user.id
            return redirect('reservas:lugares') 
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.") 
            return render(request, 'authentication/login/login.html', {'error_message': messages.get_messages(request)})
    else:
        return render(request, 'authentication/login/login.html')
    
#LOGOUT
def logoutUser(request):
    #Actualiza fecha de cierre de sesión
    if request.user.is_authenticated:
        usuario = User()
        usuario = User.objects.get(id=request.session['id'])
        print('Usuario para actualizar fecha', usuario)
        usuario.last_session = datetime.now()
        usuario.save()
    else:
        print('Según django nadie se autenticó')
    #Cierra sesión
    logout(request)
    try:
        del request.session['usuario']
    except KeyError:
        pass
    messages.success(request, 'Ha cerrado sesion')
    return render(request,'authentication/login/login.html')

   