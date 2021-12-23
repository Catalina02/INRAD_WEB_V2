from django.contrib import admin
from django.db.models import fields

from . import models
class DisponibilidadAdmin(admin.ModelAdmin):
    list_display=['Medico',]
    verbose_name='Disponibilidad'

class AgendamientoAdmin(admin.ModelAdmin):
    list_display = ['owner','paciente','dia_de_cita','hora_inicio','hora_termino','approved']
    list_editable=['approved']

admin.site.register(models.Agendamiento,AgendamientoAdmin)
admin.site.register(models.Disponibilidad,DisponibilidadAdmin)
admin.site.register(models.DiasDisponibles)
admin.site.register(models.AgendaOcupada)
