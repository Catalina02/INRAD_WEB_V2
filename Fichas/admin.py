from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


class CustomPacientAdmin(admin.ModelAdmin):
    # The forms to add and change user instances

    list_display = ('rut','nombre','apellido','email','numero_telefono','prevision')
    ordering = ("rut",)

    fieldsets = (
   
        ('Informacion Personal', {
            'fields': ('rut','nombre', 'apellido',
                       'email', 'numero_telefono', 'edad', 'fecha_nacimiento', 'direccion','alta' )
        }),
        )
    add_fieldsets = (
   
        ('Informacion Personal', {
            'fields': ('rut','nombre', 'apellido',
                       'email', 'numero_telefono', 'edad', 'fecha_nacimiento', 'direccion','alta' )
        }),
        )
    list_filter=['prevision','edad']
    filter_horizontal = ()


admin.site.register(Diagnostico)
admin.site.register(Paciente,CustomPacientAdmin)
admin.site.register(Equipo)
admin.site.register(Historia)
admin.site.register(Imagenologia)
admin.site.register(Modalidad)
admin.site.register(Observaciones)
admin.site.register(Tecnica)
admin.site.register(Tratamiento)
