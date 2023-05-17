from django.shortcuts import render, redirect
from .forms import FormularioRegistro
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Inicia sesión con tus credenciales.')
    else:
        form = FormularioRegistro()
    return render(request, 'authentication/register/register.html', {'form': form, 'messages': messages.get_messages(request)})
