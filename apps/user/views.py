from django.shortcuts import render, redirect
from .forms import FormularioRegistro

def register(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioRegistro()
    return render(request, 'authentication/register/register.html', {'form': form})
