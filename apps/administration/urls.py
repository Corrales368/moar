from django.urls import path

from apps.administration import views


app_name = 'administration'

urlpatterns = [
    path('administration/', views.AdminHomeView.as_view(), name='administration_home'),
]
