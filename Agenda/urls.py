from django.urls import path, include
from .views import abrir_agenda
from django.views.generic import RedirectView
from django.conf.urls import url

from .views import abrir_agenda

app_name='Agenda'
urlpatterns = [

    path('abrir_agenda/', abrir_agenda, name='abrir_agenda'),
 
]
