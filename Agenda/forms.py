from django import forms
from .models import Disponibilidad,Agendamiento,DiasDisponibles
from django.forms import TextInput,TimeInput,ChoiceField

class AvailabilityForm(forms.ModelForm):
    class Meta:
        #obtiene tipos de datos desde el modelo definido
        model=Disponibilidad
        fields='start_date','start_time','end_time','recurrence'
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

class AgendamientoForm(forms.ModelForm):
    def clean_dia(self):
        start_time=self.cleaned_data.get('start_time')
        end_time=self.cleaned_data.get('end_time')
        dia=self.cleaned_data.get('dia')
        medico=self.cleaned_data('Medico_id')
        #validaciones
        medselect=DiasDisponibles.objects.filter(Medico_id=medico)
        
        return self.cleaned_data
    class Meta:
        #obtiene tipos de datos desde el modelo definido
        model=Agendamiento
        fields='Medico','dia','horarios'
        widgets = {
            'dia': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccione una Fecha', 'type':'date','lang': 'es',}),
        }
        labels = {
         "Medico": "Seleccione Medico",
        }