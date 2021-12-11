from django.urls import path, include
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url

from .views import home,contacto,nosotros,tratamientos,pacientes,terapias

app_name='Web'
urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    path('tratamientos/', views.tratamientos, name='tratamientos'),
    path('terapias/', terapias, name='terapias'),
    path('pacientes/', pacientes, name='pacientes'),
]
