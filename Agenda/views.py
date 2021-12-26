from django.shortcuts import redirect, render, get_object_or_404
from Agenda.forms import AvailabilityForm,AgendamientoForm,AgendamientoEditForm
from Agenda.models import Agendamiento, DiasDisponibles, Disponibilidad,AgendaOcupada
import pytz
import sweetify
from django import forms
from datetime import datetime, timezone
import pytz
from django_agenda.time_span import TimeSpan
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
            sweetify.success(request, 'Agenda Abierta',icon='success')
            return redirect('Web:home')
            data['form']=formulario
        else:
            data['form']=formulario

    return render(request,'abrir_agenda.html',data)


def agendar_paso1(request):
    data={
        'form':AgendamientoForm()
    }
    if request.method=='POST':# si se reciben datos del formulario
        formulario=AgendamientoForm(data=request.POST)
        if formulario.is_valid():
            formulario.instance.paciente = request.user
            formulario.instance.start_time=datetime.strptime(formulario.instance.dia.strftime('%Y%m%d ')+formulario.instance.horarios[:5] ,'%Y%m%d %H:%M').astimezone( pytz.timezone('UTC'))
            formulario.instance.end_time=datetime.strptime(formulario.instance.dia.strftime('%Y%m%d ')+formulario.instance.horarios[-5:] ,'%Y%m%d %H:%M').astimezone( pytz.timezone('UTC'))
            formulario.instance.approved=True
            try:
                formulario.instance.clean()
            except:
                sweetify.error(request, 'Horario Ocupado',icon='error')
                return redirect('Agenda:agendar_paso1')
            formulario.save()
            data['form']=formulario
            sweetify.success(request, 'Agendado con Exito',icon='success')
            return redirect('Web:home')
        else:
            data['form']=formulario
    return render(request,'agendar_paso1.html',data)

def modificar_hora(request,id):
    agenda=get_object_or_404(Agendamiento,id=id)
    data={
        'form':AgendamientoForm(instance=agenda)
    }
    if request.method=='POST':# si se reciben datos del formulario
        formulario=AgendamientoForm(data=request.POST,instance=agenda)
        ocupado=AgendaOcupada.objects.filter(booking_id=id)[0]
        if formulario.is_valid():
            formulario.instance.paciente = request.user
            formulario.instance.start_time=datetime.strptime(formulario.instance.dia.strftime('%Y%m%d ')+formulario.instance.horarios[:5] ,'%Y%m%d %H:%M').astimezone( pytz.timezone('UTC'))
            formulario.instance.end_time=datetime.strptime(formulario.instance.dia.strftime('%Y%m%d ')+formulario.instance.horarios[-5:] ,'%Y%m%d %H:%M').astimezone( pytz.timezone('UTC'))
            formulario.instance.approved=True
            try:
                formulario.instance.clean()
            except:
                sweetify.error(request, 'Horario Ocupado',icon='error')
                return redirect('/modificar_hora/'+id)
            ocupado.start=formulario.instance.start_time
            ocupado.end=formulario.instance.end_time
            formulario.save()
            data['form']=formulario
            sweetify.success(request, 'Agendado con Exito',icon='success')
            return redirect('AppUsers:profile')
            
    return render(request,'modificar_hora.html',data)

def eliminar_hora(request,id):
    agenda=get_object_or_404(Agendamiento,id=id)
    ocupado=AgendaOcupada.objects.filter(booking_id=id)
    agenda.delete()
    ocupado.delete()
    sweetify.success(request, 'Eliminado con Exito',icon='success')
    return redirect(to='AppUsers:profile')