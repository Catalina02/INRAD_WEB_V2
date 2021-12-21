from django.urls import path, include
from .views import agendar
from django.views.generic import RedirectView
from django.conf.urls import url

from .views import agendar

app_name='Agenda'
urlpatterns = [

    path('agendar/', agendar, name='agendar'),
 
]
