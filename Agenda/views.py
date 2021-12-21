from django.shortcuts import render
from Agenda.forms import AvailabilityForm
import sweetify
# Create your views here.
def agendar(request):
    data={
        'form':AvailabilityForm()
    }
    if request.method=='POST':# si se reciben datos del formulario
        formulario=AvailabilityForm(data=request.POST) #entrega lo que hat en post(datos de formularp)
        if formulario.is_valid():
            formulario.save()
            sweetify.success(request, 'Mensaje Enviado',icon='success')

        else:
            data['form']=formulario
    return render(request,'agendar.html',data)