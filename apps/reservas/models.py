# Create your models here.
from django.db import models
from ..user.models import User


class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='img/bg-img/', default='img/bg-img/feature-1.jpg')
    
    def __str__(self):
        return self.nombre

class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    numero_habitacion = models.IntegerField()
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Habitación {self.numero} - {self.hotel.nombre}'

class Reservacion(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    huesped = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.IntegerField(default=0)
    adults = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Reservación {self.id} - {self.habitacion}'
