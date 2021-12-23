from django.contrib import admin
from django.db.models import fields

from . import models
class Disaponibilidad(admin.ModelAdmin):
    list_display=['Medico',]
    verbose_name='Disponibilidad'

class Agendamientos(admin.ModelAdmin):
    list_display = ['owner','start_time',"end_time",'approved']


admin.site.register(models.Agendamiento)
admin.site.register(models.Availability)
admin.site.register(models.AvailabilityOccurrence,Disaponibilidad)
admin.site.register(models.Slot)
