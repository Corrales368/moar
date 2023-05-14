from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.core.exceptions import ValidationError  

class FormularioRegistro(UserCreationForm):

    class Meta:
        model = User
        fields = ('__all__')
       

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
    
    def name_clean(self):  
        name = self.cleaned_data['name'].lower()  
        return name

    def last_name_clean(self):  
        last_name = self.cleaned_data['last_name'].lower()  
        return last_name


    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("As senhas não correspondem")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],
            name=self.cleaned_data['name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )  
        return user     
    
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"

   
