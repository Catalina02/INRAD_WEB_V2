from django.contrib import admin

from . import models

admin.site.register(models.Booking)
admin.site.register(models.Availability)
admin.site.register(models.AvailabilityOccurrence)
admin.site.register(models.Slot)
