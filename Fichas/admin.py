from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class DiagnosticoInline(admin.StackedInline):
    model=Diagnostico
    extra=0
    fields=['descripcion',]

class TratamientoInline(admin.StackedInline):
    model=Tratamiento
    extra=0
    fields=['energia','zona_irradiada','dosis','profundidad_calculo','interrupciones','localizacion','fecha_inicio','fecha_termino',]
    
class HistoriaInline(admin.StackedInline):
    model=Historia
    extra=0
    fields=['descripcion',]
class ImagenesInline(admin.StackedInline):
    model=Imagenologia
    extra=0
    fields=['ruta',]
class ObservacionesInline(admin.StackedInline):
    model=Observaciones
    extra=0
    fields=['descripcion',]

class CustomTratamientoAdmin(admin.ModelAdmin):
    #inlines=[TecnicaInline,EquipoInline,ModalidadInline]
    list_display = ['energia','zona_irradiada','interrupciones','localizacion','fecha_inicio','fecha_termino']
    fieldsets = (
        ('Informacion del Tratamiento', {
            'fields': ('energia','zona_irradiada','dosis','profundidad_calculo','interrupciones','localizacion','fecha_inicio','fecha_termino')
        }),
        )
class CustomPacientAdmin(admin.ModelAdmin):
    #Inlines: mostrar datos obtenedos de modelos heredados
    inlines=[DiagnosticoInline,HistoriaInline,ImagenesInline,ObservacionesInline,TratamientoInline,]
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



admin.site.register(Paciente,CustomPacientAdmin)

admin.site.register(Tratamiento,CustomTratamientoAdmin)
