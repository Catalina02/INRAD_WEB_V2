from django.contrib import admin
from django.db.models import fields

from . import models
class Disaponibilidad(admin.ModelAdmin):
    list_display=['Medico',]

admin.site.register(models.Booking)
admin.site.register(models.Availability)
admin.site.register(models.AvailabilityOccurrence,Disaponibilidad)
admin.site.register(models.Slot)
