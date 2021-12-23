from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Administrativo, UsuarioPaciente, Usuario,Medico,Administrativo#,InformacionMedica
from Fichas.models import *
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin

'''****************** Admnistracion basica ususarios*******************************************************'''
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('rut','email')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

'''****************** manejo PACIENTES panel administracion*******************************************************'''
#Habilita el Uso de Campos Extras al Modelo Usuario
'''
class UsuarioPacienteInformacionMedicaInline(admin.StackedInline):
    model = InformacionMedica

class UsuarioPacienteAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    inlines = (
        UsuarioPacienteInformacionMedicaInline,
    )
'''
#DESPLIEGA LA INFO TOTAL DEL PACIETNE
class CustomPacienteAdmin(ImportExportModelAdmin,UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ('rut','dv','nombre','apellido_paterno','apellido_materno','sexo','email','telefono_contacto','prevision')
    ordering = ("rut",)
    #inlines = (
    #    UsuarioPacienteInformacionMedicaInline,
    #)
    fieldsets = (
        ('Informacion de Perfil', {
            'fields': ('rut','dv', 'password')
        }),
        ('Informacion Personal', {
            'fields': ('nombre', 'apellido_paterno','apellido_materno',
                       'email', 'telefono_contacto', 'telefono_contacto_2','sexo', 'fecha_nacimiento', 'foto_perfil', 'type')
        }),
        )
    add_fieldsets = (
        ('Informacion de Perfil', {
            'fields': ('rut','dv', 'password', )
        }),
        ('Informacion Personal', {
            'fields': ('nombre', 'apellido_paterno','apellido_materno',
                       'email', 'telefono_contacto', 'telefono_contacto_2','sexo', 'fecha_nacimiento', 'foto_perfil', )
        }),
        )
    list_filter=['prevision','date_joined']
    filter_horizontal = ()

'''****************** manejo ADMINISTRATIVOS panel administracion*******************************************************'''

#Desplagar Informacion solo de Usuarios
class CustomAdministrativoAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ('rut','dv','nombre','apellido_paterno','apellido_materno','sexo','email','telefono_contacto','prevision')
    ordering = ("rut",)

    fieldsets = (
        ('Informacion de Perfil', {
            'fields': (('rut','dv'), 'password')
        }),
        ('Informacion Personal', {
            'fields': ('nombre', 'apellido_paterno','apellido_materno',
                       'email', 'telefono_contacto', 'telefono_contacto_2','sexo', 'fecha_nacimiento', 'foto_perfil', )
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', )
        }),
        ('Grupos', {
            'fields': ('groups', 'type' )
        }),
        ('Fechas Importantes', {
            'fields': (('date_joined',), )
        }),
    
    )
    add_fieldsets =(
        (None, {
            # 'classes': ('collapse',),
            'fields':(('rut','dv'), 'password')
        }),
        ('Informacion Personal', {
            'fields': ('nombre', 
                        'apellido_paterno','apellido_materno',
                       'email', 'sexo', 'fecha_nacimiento', 'foto_perfil', )
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', )
        }),
        ('Grupos', {
            'fields': ('groups', 'type' )
        }),
        ('Fechas Importantes', {
            'fields': (('date_joined',), )
        }),
    
    )
    list_filter=['prevision','date_joined']
    filter_horizontal = (('groups',  ))
   
'''****************** manejo MEDICOS panel administracion*******************************************************'''
#Habilita el Uso de Campos Extras al Modelo Usuario

#DESPLIEGA LA INFO TOTAL DEL PACIETNE
class CustomMedicoAdmin(ImportExportModelAdmin,UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ('rut','dv','nombre','apellido_paterno','apellido_materno','sexo','email','telefono_contacto','prevision')
    ordering = ("rut",)

    fieldsets = (
        ('Informacion de Perfil', {
            'fields': (('rut','dv'), 'password')
        }),
        ('Informacion Personal', {
            'fields': ('nombre', 'apellido_paterno','apellido_materno',
                       'email', 'telefono_contacto', 'telefono_contacto_2','sexo', 'fecha_nacimiento', 'foto_perfil', )
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', )
        }),
        ('Grupos', {
            'fields': ('groups',  'type')
        }),
        ('Fechas Importantes', {
            'fields': (('date_joined',), )
        }),
    
    )
    add_fieldsets =(
        (None, {
            # 'classes': ('collapse',),
            'fields':(('rut','dv'), 'password')
        }),
        ('Informacion Personal', {
            'fields': ('nombre', 
                        'apellido_paterno','apellido_materno',
                       'email', 'sexo', 'fecha_nacimiento', 'foto_perfil', )
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', )
        }),
        ('Grupos', {
            'fields': ('groups', 'type' )
        }),
        ('Fechas Importantes', {
            'fields': (('date_joined',), )
        }),
    
    )
    list_filter=['prevision','date_joined']
    filter_horizontal = (('groups',  ))




admin.site.register(UsuarioPaciente, CustomPacienteAdmin)
admin.site.register(Medico, CustomMedicoAdmin)
admin.site.register(Administrativo, CustomAdministrativoAdmin)

  


#admin.site.register(Usuario,UsuarioAdmin)

