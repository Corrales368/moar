from django.shortcuts import render
from .models import *
from .forms import ReservasForm
from django.contrib import messages
#Decoradores
from django.contrib.auth.decorators import login_required

# Create your views here.
def lugaresPage(request):
    hotel = Hotel.objects.all()
    context = {'hotel': hotel}   
    return render(request, 'reservas/lugares.html',context)

def contactPage(request):  
    return render(request, 'reservas/contact.html')

@login_required(login_url='authentication:login')
def reservasPage(request):
    if request.method == 'POST':
        form = ReservasForm(request.POST)
        print(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False) 
            reserva.huesped = User.objects.get(id=request.session['id'])
            reserva.save() 
            messages.success(request, '¡Reserva exitosa!')
    else:
        form = ReservasForm()
    return render(request, 'reservas/reservar.html', {'form': form, 'messages': messages.get_messages(request)})
