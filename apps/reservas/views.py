from django.shortcuts import render
from .models import *
from .forms import ReservasForm
from django.contrib import messages

# Create your views here.
def lugaresPage(request):
    hotel = Hotel.objects.all()
    context = {'hotel': hotel}   
    return render(request, 'reservas/lugares.html',context)

def contactPage(request):  
    return render(request, 'reservas/contact.html')

def reservasPage(request):
    if request.method == 'POST':
        form = ReservasForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Reserva exitosa!')
    else:
        form = ReservasForm()
    return render(request, 'reservas/reservar.html', {'form': form, 'messages': messages.get_messages(request)})
