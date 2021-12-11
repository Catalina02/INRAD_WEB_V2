from django import forms
from django.contrib.auth.forms import UserCreationForm
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
        