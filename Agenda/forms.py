from django import forms
from .models import Availability

class AvailabilityForm(forms.ModelForm):
    class Meta:
        #obtiene tipos de datos desde el modelo definido
        model=Availability
        fields='start_date',
        
        
