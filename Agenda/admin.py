from django.contrib import admin
from django.db.models import fields

from . import models
class DisponibilidadAdmin(admin.ModelAdmin):
    list_display= ['Medico','nombre_medico','hora_inicio','hora_termino','dia_de_inicio','dia_de_termino','numero_telefono','correo_electronico']
    verbose_name='Disponibilidad'
    
    search_fields=['Medico','nombre_medico']
    list_per_page=50

class DiasDisponiblesAdmin(admin.ModelAdmin):
    list_display= ['Medico','nombre_medico','hora_inicio','hora_termino','dia','numero_telefono','correo_electronico']
    verbose_name='Disponibilidad'
    list_filter=['Medico',]
    search_fields=['Medico','nombre_medico']
    list_per_page=50

class AgendamientoAdmin(admin.ModelAdmin):
    list_display = ['paciente','nombre_paciente','dia_de_cita','hora_inicio','hora_termino','approved','numero_telefono','correo_electronico']
    list_editable=['approved']
    list_filter=['approved','owner']
    search_fields=['paciente','nombre_paciente']
    list_per_page=50
  
class AgendaOcupadaAdmin(admin.ModelAdmin):
    list_display = ['paciente','nombre_paciente','dia_de_cita','hora_inicio','hora_termino','numero_telefono','correo_electronico']
    search_fields=['paciente','nombre_paciente']
    list_per_page=50

admin.site.register(models.Agendamiento,AgendamientoAdmin)
admin.site.register(models.Disponibilidad,DisponibilidadAdmin)
admin.site.register(models.DiasDisponibles,DiasDisponiblesAdmin)
admin.site.register(models.AgendaOcupada,AgendaOcupadaAdmin)
