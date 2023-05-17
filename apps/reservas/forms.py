from django import forms
from .models import *
from django import forms  
from django.db import models
from django.forms import ModelForm

class ReservasForm(ModelForm):
    class Meta:
        model = Reservacion
        fields =  ('habitacion', 'fecha_inicio', 'fecha_fin','huesped','rooms', 'adults')
    
    habitacion = forms.ModelChoiceField(queryset = Habitacion.objects.all(), empty_label="Selecione...", )
    fecha_inicio = forms.DateField(label='',)
    fecha_fin= forms.DateField(label='',)
    huesped = forms.IntegerField(label='')
    rooms = forms.IntegerField(label='')
    adults = forms.IntegerField(label='')

   