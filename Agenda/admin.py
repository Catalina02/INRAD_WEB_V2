from django.contrib import admin
from django.db.models import fields
from django.contrib.admin import DateFieldListFilter
from . import models

from Users.models import Medico

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DiasDisponiblesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ['rut_medico','Medico','__str__','hora_inicio','hora_termino','numero_telefono','correo_electronico']
    verbose_name='Disponibilidad'
    list_filter=['Medico__apellido_paterno',('start', DateFieldListFilter)]
    ordering = ('start','Medico__rut')
    search_fields=['Medico__nombre','Medico__apellido_paterno','Medico__apellido_materno','medico__rut']
    list_per_page=100
    fieldsets = (
        
        ('Informacion de Medico', {
            'fields': ('Medico',)
        }),
        ('Informacion de Atención', {
            'fields': ('start','end')
        }),
    )

class AgendamientoAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['rut_paciente','paciente','dia_de_cita','hora_inicio','hora_termino','approved','numero_telefono','correo_electronico','medico_a_cargo','modificado']
    list_editable=['approved']
    list_filter=['approved','Medico__apellido_paterno','dia']
    search_fields=['Medico__nombre','Medico__apellido_paterno','Medico__apellido_materno','paciente__nombre','paciente__apellido_paterno','paciente__apellido_materno','paciente__rut','Medico__rut']
    ordering = ('start_time',"paciente")
    list_per_page=50
    fieldsets = (
        ('Informacion de Paciente', {
            'fields': ('paciente','motivo_consulta')
        }),
        ('Informacion de Medico', {
            'fields': ('Medico','disponibilidad')
        }),
        ('Informacion de Consulta', {
            'fields': ('start_time','end_time')
        }),
         ('Informacion de Extra', {
            'fields': ('modificado','motivo_modificacion')
        }),
        ('CONFIRMACION', {
            'fields': ('approved',)
        }),
    )
        
  
class AgendaOcupadaAdmin(admin.ModelAdmin):
    list_display = ['rut_paciente','nombre_paciente','dia_de_cita','hora_inicio','hora_termino','numero_telefono','correo_electronico','medico_a_cargo']
    list_filter=['start','Medico__apellido_paterno']
    search_fields=['Medico__nombre','Medico__apellido_paterno','Medico__apellido_materno','booking__paciente__nombre','booking__paciente__apellido_paterno','booking__paciente__apellido_materno','paciente__rut','medico__rut']
    list_per_page=100
#Considero que es inncessesario mmosttarla pues es la misma info que Citas Agendadas
#admin.site.register(models.AgendaOcupada,AgendaOcupadaAdmin)


class CitasCanceladasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['rut_paciente','paciente','dia_cita','hora_inicio_cita','hora_termino_cita','medico','resuelto','numero_telefono','correo_electronico']
    list_filter=['resuelto','medico__apellido_paterno','dia_cita']
    search_fields=['medico__nombre','medico__apellido_paterno','medico__apellido_materno','paciente__nombre','paciente__apellido_paterno','paciente__apellido_materno','paciente__rut','medico__rut']
    list_editable=['resuelto']
    list_per_page=100
    fieldsets = (
        ('Informacion de Paciente', {
            'fields': ('paciente',)
        }),
        ('Informacion de Consulta Cancelada', {
            'fields': ('dia_cita',('hora_inicio_cita','hora_termino_cita'),'motivo_cita')
        }),
        ('Informacion de Cancelación', {
            'fields': ('motivo_cancelacion',)
        }),
        ('Estado de Cancelacion', {
            'fields': ('resuelto',)
        }),
    )

admin.site.register(models.Agendamiento,AgendamientoAdmin)
admin.site.register(models.DiasDisponibles,DiasDisponiblesAdmin)
admin.site.register(models.CitasCanceladas,CitasCanceladasAdmin)
