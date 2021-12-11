from django.shortcuts import render
from .forms import  MensajeForm
from django.contrib import messages
import sweetify
from datetime import datetime

def home(request):
    return render(request, 'inicio.html')

def contacto(request):
    data={
        'form':MensajeForm()
    }
    if request.method=='POST':# si se reciben datos del formulario
        formulario=MensajeForm(data=request.POST) #entrega lo que hat en post(datos de formularp)
        if formulario.is_valid():
            formulario.instance.fecha_contacto=datetime.today().strftime('%Y-%m-%d') 
            formulario.save()
            data['mensaje']='Mensaje Guardado'
            sweetify.success(request, 'Mensaje Enviado',icon='success')

        else:
            data['form']=formulario

    return render(request,'contacto.html',data)
 
def nosotros(request):
    return render(request,'nosotros.html')
 
def tratamientos(request):
    return render(request,'tratamientos.html')

def terapias(request):
    return render(request,'terapias.html')
 
def pacientes(request):
    return render(request,'pacientes.html')
 
