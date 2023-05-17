from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.core.exceptions import ValidationError  

class FormularioRegistro(UserCreationForm):
    class Meta: 
        model = User
        fields =  ('username', 'first_name', 'last_name','fecha_nacimiento','email', 'password1', 'password2', 'direccion', 'telefono', 'tipo_cedula', 'numero_cedula')

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("Usuário já existe")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("O e-mail já existe")     
        return email  


    def last_name_clean(self):  
        last_name = self.cleaned_data['last_name'].lower()  
        return last_name


    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las contraseñas no coinciden")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
           
            self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name = self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            direccion=self.cleaned_data['direccion'],
            telefono=self.cleaned_data['telefono'],
            tipo_cedula=self.cleaned_data['tipo_cedula'],
            numero_cedula=self.cleaned_data['numero_cedula'],
           
        )  
        return user     
    
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"

   
