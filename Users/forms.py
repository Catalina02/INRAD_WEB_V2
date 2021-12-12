from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from .models import Usuario
from .validators import MaxSizeImgValidator
from django.forms import TextInput, EmailInput
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError
from itertools import cycle
from phonenumber_field.modelfields import PhoneNumberField


#Registro de Usuaruio
class CustomUserCreationForm(UserCreationForm):
    rut=forms.IntegerField(min_value=5,max_value=99999999,widget=forms.TextInput(attrs={'placeholder': 'Rut sin puntos, sin guión y sin dv', 'style': 'text-align:left;'}))
    dv=forms.CharField(max_length=1)
    foto_perfil=forms.ImageField(required=False,validators=[MaxSizeImgValidator(max_file_size=2)])
 
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
        

class CustomUserEditionForm(UserChangeForm):
    template_name='/something/else'
    class Meta:
        model=Usuario
        fields=['foto_perfil','nombre','apellido_paterno','apellido_materno','sexo','email','telefono_contacto','telefono_contacto_2','domicilio','prevision']
        exclude=['rut','dv','password','password1','password2']
   
    '''
    def save(self,commit=True):
        user=super(CustomUserEditionForm,self).save(commit=False)
        user.foto_perfil=self.cleaned_data['foto_perfil']
        user.nombre=self.cleaned_data['nombre']
        user.apellido_paterno=self.cleaned_data['apellido_paterno']
        user.apellido_materno=self.cleaned_data['apellido_materno']
        user.sexo=self.cleaned_data['sexo']
        user.email=self.cleaned_data['email']
        user.telefono_contacto=self.cleaned_data['telefono_contacto']
        user.telefono_contacto_2=self.cleaned_data['telefono_contacto_2']
        user.domicilio=self.cleaned_data['domicilio']
        user.prevision=self.cleaned_data['prevision']

        if commit:
            user.save()
        return user
    '''