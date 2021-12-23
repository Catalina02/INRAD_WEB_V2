from django import forms
from .models import Disponibilidad
from django.forms import TextInput,TimeInput
class AvailabilityForm(forms.ModelForm):
    class Meta:
        #obtiene tipos de datos desde el modelo definido
        model=Disponibilidad
        fields='start_date','start_time','end_time','duracion_cita','recurrence'
        exclude = 'Medico',
        widgets = {
            'start_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccione una Fecha', 'type':'date','lang': 'es',}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
        "start_date": "Dia de Inicio",
        'start_time':'Hora Inicio Jornada',
        'end_time':'Hora Termino Jornada',
        'recurrence':'Otorgar Recurrencia'
        }