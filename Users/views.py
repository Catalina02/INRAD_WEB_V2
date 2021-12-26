from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserEditionForm,PasswordChangeForm
from django.shortcuts import redirect, render
from Agenda.models import Agendamiento
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
import sweetify
from datetime import datetime



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
    user=request.user.id
    agendas=Agendamiento.objects.filter(paciente_id=user).order_by('dia')
    data={
        'agendas':agendas
    }
    return render(request,'profile.html',data)


def logoutView(request):
    logout(request)
    sweetify.success(request, 'Sesión Cerrada Correctamente',icon='success')
    return redirect('Web:home')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            form.user.foto_perfil = form.cleaned_data['foto_perfil']
            sweetify.success(request, 'Contraseña Modificada Correctamente',icon='success')
            update_session_auth_hash(request, form.user)
            return redirect(reverse('AppUsers:profile'))
        else:
            sweetify.success(request, 'Error, Intente Nuevamente',icon='error')
            return redirect(reverse('AppUsers:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)





def edit_profile(request    ):
    if request.method=='POST':
        formulario=CustomUserEditionForm(request.POST,request.FILES,instance=request.user)
        if formulario.is_valid():
            formulario.save()
            sweetify.success(request, 'Datos Modificados Correctamente',icon='success')
            #return HttpResponseRedirect(reverse_lazy('AppUsers:profile'))
            return redirect('AppUsers:profile')
        else:
            sweetify.error(request, 'Telefono Ingresado Incorrecto',icon='error')
            return redirect('AppUsers:edit_profile')
    else:
        formulario=CustomUserEditionForm(instance=request.user)
        data={'form':formulario}
        return render(request, 'edit_profile.html',data)
    
