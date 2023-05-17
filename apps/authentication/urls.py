from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('PasswordResetForm/',views.PasswordResetForm, name='PasswordResetForm'),
    path('PasswordReset/<str:id>/<str:token>/', views.PasswordResetConfirm, name='PasswordReset'),
]
