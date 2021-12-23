from django.urls import path, include
from .views import abrir_agenda,agendar_paso1
from django.views.generic import RedirectView
from django.conf.urls import url
from django.views.i18n import JavaScriptCatalog


app_name='Agenda'
urlpatterns = [

    path('abrir_agenda/', abrir_agenda, name='abrir_agenda'),
    path('agendar_step_1/', agendar_paso1, name='agendar_paso1'),
 
]

js_info_dict = {
'packages': ('recurrence', ),
}
# jsi18n can be anything you like here
urlpatterns += [
url(r'^jsi18n/$', JavaScriptCatalog.as_view(), js_info_dict),
]