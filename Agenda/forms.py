from django import forms
from .models import Disponibilidad,Agendamiento,DiasDisponibles,CitasCanceladas
from django.forms import TextInput, Textarea
import sweetify

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

class AgendamientoEditForm(forms.ModelForm):
    
    def cleaned_data(self):
        med = self.cleaned_data['Medico']
        dia=self.cleaned_data.get('dia')
        dd=DiasDisponibles.objects.filter(Medico_id=med)
        dias=dia.strftime('%d-%m-%Y')
        ddl=[]
        for i in dd:
            ddl.append(str(i))
        if dias  in ddl:
            approved=self.cleaned_data['approved']
            return self.cleaned_data
        else:
            raise forms.ValidationError(f'Día no Disponible')
    

    class Meta:
        #obtiene tipos de datos desde el modelo definido
        DIASDD=[]
        elegirdia = forms.ChoiceField(choices = DIASDD)
        model=Agendamiento
        fields='Medico','dia','horarios',
        widgets = {
            'dia': forms.DateInput()
        }
        labels = {
         "Medico": "Seleccione Medico",
        }

class AgendamientoForm(forms.ModelForm):
    
    def cleaned_data(self):
        med = self.cleaned_data['Medico']
        dia=self.cleaned_data.get('dia')
        dd=DiasDisponibles.objects.filter(Medico_id=med)
        dias=dia.strftime('%d-%m-%Y')
        ddl=[]
        for i in dd:
            ddl.append(str(i))
        if dias  in ddl:
            approved=self.cleaned_data['approved']
            return self.cleaned_data
        else:
            raise forms.ValidationError(f'Día no Disponible')
    

    class Meta:
        #obtiene tipos de datos desde el modelo definido
        DIASDD=[]
        elegirdia = forms.ChoiceField(choices = DIASDD)
        model=Agendamiento
        fields='Medico','dia','horarios','motivo_consulta'
        widgets = {
            'dia': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccione una Fecha', 'type':'date','lang': 'es',}),
            'motivo_consulta':forms.Textarea(attrs={'rows':2, 'cols':40}),
        }
        labels = {
         "Medico": "Seleccione Medico",
         'motivo_consulta':'Indique Motivo de Consulta Medica'
        }

class Eliminar_con_Motivo(forms.ModelForm):
    class Meta:
        model=CitasCanceladas
        fields='motivo_cancelacion',
        labels = {
         'motivo_cancelacion':'Indique Motivo de Cancelación',
        }
        widgets = {
             'motivo_cancelacion':forms.Textarea(attrs={'rows':2, 'cols':40}),
        }
    
class AgendamientoEditForm(forms.ModelForm):
    
    def cleaned_data(self):
        med = self.cleaned_data['Medico']
        dia=self.cleaned_data.get('dia')
        dd=DiasDisponibles.objects.filter(Medico_id=med)
        dias=dia.strftime('%d-%m-%Y')
        ddl=[]
        for i in dd:
            ddl.append(str(i))
        if dias  in ddl:
            approved=self.cleaned_data['approved']
            return self.cleaned_data
        else:
            raise forms.ValidationError(f'Día no Disponible')
    

    class Meta:
        #obtiene tipos de datos desde el modelo definido
        DIASDD=[]
        elegirdia = forms.ChoiceField(choices = DIASDD)
        model=Agendamiento
        fields='Medico','dia','horarios','motivo_modificacion'
        widgets = {
            'dia': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccione una Fecha', 'type':'date','lang': 'es',}),
             'motivo_modificacion':forms.Textarea(attrs={'rows':2, 'cols':40}),
        }
        labels = {
         "Medico": "Seleccione Medico",
         'motivo_modificacion':'Indique Motivo de Modificación'
        }