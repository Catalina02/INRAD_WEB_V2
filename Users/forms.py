#from _typeshed import NoneType
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from .models import Usuario
from .validators import MaxSizeImgValidator
from django.forms import TextInput, EmailInput
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError
from itertools import cycle
from phonenumber_field.modelfields import PhoneNumberField
import re

#Registro de Usuaruio
class CustomUserCreationForm(UserCreationForm):
    '''
    rut=forms.IntegerField(min_value=5,max_value=99999999,widget=forms.TextInput(attrs={'placeholder': 'Rut sin puntos, sin guión y sin dv', 'style': 'text-align:left;'}))
    dv=forms.CharField(max_length=1)'''
    foto_perfil=forms.ImageField(required=False,validators=[MaxSizeImgValidator(max_file_size=5)])

    #verificar rut
    def clean(self):
        dv=self.cleaned_data.get('dv')
        rut=self.cleaned_data.get('rut')
        
        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        s= (-s) % 11
        if (s==10):
            if(dv.lower() != 'k'):
                raise forms.ValidationError(f'El Rut Ingresado es Incorrecto')
        else:
            if (dv !=str(s)):
                raise forms.ValidationError(f'El Rut Ingresado es Incorrecto')
                
        return self.cleaned_data
    class Meta:
        model=Usuario
        fields=['rut','dv','nombre','apellido_paterno','apellido_materno','sexo','email','telefono_contacto','password1','password2']
        

class CustomUserEditionForm(forms.ModelForm):
    template_name='/something/else'
    foto_perfil=forms.FileInput(attrs= {'style':'display: none;','class':'form-control', 'required': False,})
    def clean(self):
        telefono1=self.cleaned_data.get('telefono_contacto')
        telefono2=self.cleaned_data.get('telefono_contacto_2')
        #if (len(str(telefono1.national_number))!=9):
        if (telefono1 is None):
                raise forms.ValidationError(f'El Telefono Personal es Incorrecto')
        #if (len(str(telefono2.national_number))!=9):
        if (telefono2 is None):
                raise forms.ValidationError(f'El Telefono de Emergencia es Incorrecto')
     
                
        return self.cleaned_data
    class Meta:
        model=Usuario
        fields=['nombre','apellido_paterno','apellido_materno','sexo','email','telefono_contacto','telefono_contacto_2','domicilio','prevision','fecha_nacimiento','foto_perfil']
        exclude=['rut','dv','password','password1','password2']
        widgets = {
            'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccione una Fecha', 'type':'date','lang': 'es',}),
        }
   