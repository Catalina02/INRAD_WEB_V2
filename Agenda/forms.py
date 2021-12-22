from django import forms
from .models import Availability
from django.forms import TextInput
class AvailabilityForm(forms.ModelForm):
    class Meta:
        #obtiene tipos de datos desde el modelo definido
        model=Availability
        fields='start_date','start_time','end_time','recurrence'
        exclude = 'Medico',
        widgets = {
            'start_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccione una Fecha', 'type':'date','lang': 'es',}),

        }
        
