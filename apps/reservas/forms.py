from django import forms
from .models import *
from django import forms  
from django.db import models
from django.forms import ModelForm

class ReservasForm(ModelForm):
    class Meta:
        model = Reservacion
        fields =  ('hotel','habitacion', 'fecha_inicio', 'fecha_fin', 'adults')
    
    hotel = forms.ModelChoiceField(queryset = Hotel.objects.all(), empty_label="Selecione Hotel")
    habitacion = forms.ModelChoiceField(queryset = Habitacion.objects.all(), empty_label="Selecione Habitacion", )
    fecha_inicio = forms.DateField(label='',)
    fecha_fin= forms.DateField(label='',)
    adults = forms.IntegerField(label='')

   