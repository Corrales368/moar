from django.shortcuts import render

# Create your views here.
def loginUser(request):
   
    return render(request, 'authentication/login/login.html')

def RegisterUser(request):
   
    return render(request, 'authentication/register/register.html')
