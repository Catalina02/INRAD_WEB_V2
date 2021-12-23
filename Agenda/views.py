from django.shortcuts import redirect, render
from Agenda.forms import AvailabilityForm
from Agenda.models import Disponibilidad
import sweetify
from datetime import datetime
import pytz

#manejo de fechas y tiempo
from dateutil.relativedelta import relativedelta
# Create your views here.
def abrir_agenda(request):
    data={
        'form':AvailabilityForm()
    }
    if request.method=='POST':# si se reciben datos del formulario
        formulario=AvailabilityForm(data=request.POST)
        user_type =request.user.type
        ''' if user_type is not Medico:
            sweetify.success(request, 'Usted no es Medico',icon='error')
        else:'''
        if formulario.is_valid():
            formulario.instance.Medico = request.user
            formulario.instance.timezone = 'America/Santiago'
            formulario.save()
            id_form=formulario.instance.id 
            disponible=Disponibilidad.objects.filter(id=id_form)[0]
            start_date=disponible.start_date
            start_str=start_date.strftime('%Y%m%d')
            start_date=datetime.strptime(start_str,'%Y%m%d')
            delta=relativedelta(months=+1)
            end_date=start_date+delta
            local_tz = pytz.timezone('America/Santiago')
            start_date = local_tz.localize(start_date)
            end_date = local_tz.localize(end_date)
            disponible.recreate_occurrences(start_date,end_date)
            sweetify.success(request, 'Agenda3',icon='success')
            return redirect('Web:home')
            data['form']=formulario
        else:
            data['form']=formulario
    return render(request,'abrir_agenda.html',data)