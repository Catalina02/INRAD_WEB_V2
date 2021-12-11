from django.contrib import admin
from .models import Mensaje

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django import forms

#Aciiones
def marcar_contacto(modeladmin, request, queryset):
    queryset.update(paciente_contactado=True)

marcar_contacto.short_description = 'Marcar Usuarios que ya han sido Contactados'
# Register your models here.


class ContactoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['nombre','telefono_contacto','correo_contacto','tipo_contacto','mensaje','paciente_contactado','fecha_contacto']
    list_filter=['tipo_contacto','paciente_contactado','fecha_contacto']
    search_fields=['nombre','telefono_contacto','correo_contacto','tipo_contacto']
    list_editable=['paciente_contactado']
    list_per_page=50

    actions = [marcar_contacto]


admin.site.register(Mensaje,ContactoAdmin)
