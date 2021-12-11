from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from datetime import datetime
import sweetify
from django.contrib.auth import logout
from WebApp.views import home
from .models import Usuario,Paciente
def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            sweetify.success(request, 'Registrado con Exito',icon='success')
            user = authenticate(username=formulario.cleaned_data['rut'],password=formulario.cleaned_data['password1'])
            formulario.instance.date_joined=datetime.today().strftime('%Y-%m-%d') 
            login(request,user)
            return redirect(to="Web:home")
        data['form']=formulario

    return render(request, 'registration/registro.html',data)

     
def profile(request):
    return render(request,'profile.html')


def logoutView(request):
    logout(request)
    sweetify.success(request, 'Sesión Cerrada Correctamente',icon='success')
    return redirect('Web:home')