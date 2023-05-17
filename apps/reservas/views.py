from django.shortcuts import render

# Create your views here.
def lugaresPage(request):   
    return render(request, 'reservas/lugares.html')

def contactPage(request):  
    return render(request, 'reservas/contact.html')

def reservasPage(request):  
    return render(request, 'reservas/reservar.html')
