from django.urls import path, include
from .views import abrir_agenda,agendar_paso1,modificar_hora,eliminar_hora
from django.views.generic import RedirectView
from django.conf.urls import url
from django.views.i18n import JavaScriptCatalog


app_name='Agenda'
urlpatterns = [

    path('abrir_agenda/', abrir_agenda, name='abrir_agenda'),
    path('agendar_paso1/', agendar_paso1, name='agendar_paso1'),
    path('agendar_paso2/', agendar_paso1, name='agendar_paso2'),
    path('modificar_hora/<id>/', modificar_hora, name='modificar_hora'),
    path('eliminar_hora/<id>/', eliminar_hora, name='eliminar_hora'),
 
]

js_info_dict = {
'packages': ('recurrence', ),
}
# jsi18n can be anything you like here
urlpatterns += [
url(r'^jsi18n/$', JavaScriptCatalog.as_view(), js_info_dict),
]