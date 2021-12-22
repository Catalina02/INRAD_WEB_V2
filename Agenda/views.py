from django.shortcuts import render
from Agenda.forms import AvailabilityForm
import sweetify
# Create your views here.
def agendar(request):
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
            formulario.instance.tzinfo = 'America/Santiago'
            formulario.save()
            start_date = request.POST['start_date']
            start_date = request.POST['start_date']
            recurrence= request.POST['recurrence']
            sweetify.success(request, 'Agenda3'+recurrence,icon='success')
            data['form']=formulario
        else:
            data['form']=formulario
    return render(request,'agendar.html',data)