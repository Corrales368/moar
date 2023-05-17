from django import forms
from .models import *
from django import forms  
from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError 

class ResetPassword(forms.Form):

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    
   
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("As senhas não correspondem")  
        return password2   

class ResetPasswordForm2(forms.Form):
    
    email = forms.EmailField(label='email') 
