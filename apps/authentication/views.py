from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ..user.models import User
from datetime import datetime
from django.conf import settings
from .forms import ResetPassword, ResetPasswordForm2
#emails
from uuid import uuid4
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['usuario']=user.username
            request.session['id']=user.id
            return redirect('reservas:lugares') 
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.") 
            return render(request, 'authentication/login/login.html', {'error_message': messages.get_messages(request)})
    else:
        return render(request, 'authentication/login/login.html')
    
#LOGOUT
def logoutUser(request):
    #Actualiza fecha de cierre de sesión
    if request.user.is_authenticated:
        usuario = User()
        usuario = User.objects.get(id=request.session['id'])
        print('Usuario para actualizar fecha', usuario)
        usuario.last_session = datetime.now()
        usuario.save()
    else:
        print('Según django nadie se autenticó')
    #Cierra sesión
    logout(request)
    try:
        del request.session['usuario']
    except KeyError:
        pass
    messages.success(request, 'Ha cerrado sesion')
    return render(request,'authentication/login/login.html')

def send_email_reset(url , mail, id, name):
    #url
    URL = url
    #Generar token
    User.token = uuid4()
    User.save
    print('este es',mail)

    context = {'mail': mail,
    'link_reset': 'http://{}/PasswordReset/{}/'.format(URL, str(id) + '/' + str(User.token)),
    'link_home': 'http://{}'.format(URL),
    'name' : name
    }
    print( 'http://{}/PasswordReset/{}/'.format(URL, str(id) + '/' + str(User.token)))

    template = get_template('authentication/reset_password/template_email.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Solicitud de cambio de contraseña',
        'Moar',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

#PLANTILLA ENVIAR CORREO
def PasswordResetForm(request):

    #FORMULARIO
    form = ResetPasswordForm2(request.POST)
    borrar = request.POST.copy()
    form = ResetPasswordForm2(borrar)

    validacion = ''

    if request.method == 'POST':

        #Valida si el correo existe
        validacion = User.objects.filter(email=request.POST.get('email')).exists()

        print("validacion = ", validacion)

        if form.is_valid() and validacion == True:

            #captura ruta(Si el servidor esta en produccion coje la url del servidor)
            #URL = request.META['HTTP_HOST']
            URL = settings.DOMAIN if not settings.DEBUG else request.META['HTTP_HOST']
            #captura email ingresado
            mail = request.POST['email']
            #instancia de User
            idUser = User.objects.get(email=mail)
            #captura el id del usuario a restablecer
            id = idUser.id
            name = idUser.username
            #Genera token de seguridad
            token =  User.token = uuid4()
            User.save
            #asigna token y id a la funcion reset
            PasswordResetConfirm(request, id, token)
            #Envia el email
            send_email_reset(URL , mail, id, name)
            messages.success(request, f'se envio email de recuperacion')
            form = ResetPasswordForm2()
            print("id", id)
    else:
        form = ResetPasswordForm2()
    return render (request,'authentication/reset_password/password_reset_form.html', {'form': form, 'validacion' : validacion})

#PLANTILLA RECUPERAR CONTRASEÑA(es el link que lleva a la plantilla password_reset_confirm)
def PasswordResetConfirm(request, id, token):

    print(id)

    form = ResetPassword(request.POST)
    borrar = request.POST.copy()
    form = ResetPassword(borrar)
    if request.method == 'POST':

        if form.is_valid():
            userReset = User.objects.filter(id=id)
            if userReset.exists():
                userReset = userReset.first()
                userReset.set_password(form.cleaned_data.get('password1'))
                userReset.save()
                form = ResetPassword()
            messages.success(request, f'se cambio la contraseña')
    else:
        form = ResetPassword()
    ctx = {
        'id':id,
        'token': token,
        'form' : form,
     }
    return render (request,'authentication/reset_password/password_reset_confirm.html', ctx)

