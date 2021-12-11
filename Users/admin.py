from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Administrativo, Paciente, Usuario,Medico,Administrativo,InformacionMedica
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Autenticacion dentro de la Consola Administrador
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

#Habilita el Uso de Campos Extras al Modelo Usuario
class PacienteInformacionMedicaInline(admin.StackedInline):
    model = InformacionMedica

class PacienteAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    inlines = (
        PacienteInformacionMedicaInline,
    )
#DESPLIEGA LA INFO TOTAL DEL PACIETNE
class CustomPacientAdmin(ImportExportModelAdmin,UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ('rut','dv','nombre','apellido_paterno','apellido_materno','sexo','email','telefono_contacto','prevision')
    ordering = ("rut",)
    inlines = (
        PacienteInformacionMedicaInline,
    )
    fieldsets = (
        ('Informacion de Perfil', {
            'fields': ('rut','dv', 'password')
        }),
        ('Informacion Personal', {
            'fields': (('nombre', 'apellido_paterno','apellido_materno'),
                       'email', 'telefono_contacto', 'telefono_contacto_2','sexo', 'fecha_nacimiento', 'foto_perfil', )
        }),
        )
    add_fieldsets = (
        ('Informacion de Perfil', {
            'fields': ('rut','dv', 'password')
        }),
        ('Informacion Personal', {
            'fields': (('nombre', 'apellido_paterno','apellido_materno'),
                       'email', 'telefono_contacto', 'telefono_contacto_2','sexo', 'fecha_nacimiento', 'foto_perfil', )
        }),
        )
    list_filter=['prevision','date_joined']
    filter_horizontal = ()


#Desplagar Informacion solo de Usuarios
class CustomUserAdmin(ImportExportModelAdmin,UserAdmin):
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
            'fields': ('groups',  )
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
            'fields': ('groups',  )
        }),
        ('Fechas Importantes', {
            'fields': (('date_joined',), )
        }),
    
    )
    list_filter=['prevision','date_joined']
    filter_horizontal = (('groups',  ))
   

admin.site.register(Paciente, CustomPacientAdmin)
admin.site.register(Medico, CustomUserAdmin)
admin.site.register(Administrativo, CustomUserAdmin)
  

#admin.site.register(Usuario,UsuarioAdmin)

