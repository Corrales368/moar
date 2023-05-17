from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from uuid import uuid4
import uuid
class User(AbstractUser):
    # ... otros campos y métodos ...

    groups = models.ManyToManyField(Group, related_name='authentication_user')
    user_permissions = models.ManyToManyField(Permission, related_name='authentication_user_permissions')
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    CEDULA_CHOICES = (
        ('', 'Tipo de cedula'),
        ('1', 'Cedula de Ciudadania'),
        ('2', 'Tarjeta de Identidad'),
        ('3', 'Cedula de Extranjeria'),
    )

    tipo_cedula = models.CharField(max_length=1, choices=CEDULA_CHOICES,blank=True)
    numero_cedula = models.CharField(max_length=12, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)