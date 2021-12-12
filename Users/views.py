from .forms import CustomUserCreationForm, CustomUserEditionForm,PasswordChangeForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from WebApp.views import home
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
    return render(request,'profile.html')


def logoutView(request):
    logout(request)
    sweetify.success(request, 'Sesión Cerrada Correctamente',icon='success')
    return redirect('Web:home')

def edit_profile(request):
    if request.method=='POST':
        formulario=CustomUserEditionForm(request.POST,instance=request.user)
        if formulario.is_valid():
            formulario.save()
            sweetify.success(request, 'Datos Modificados Correctamente',icon='success')
            return redirect(to="AppUsers:profile")
    else:
        formulario=CustomUserEditionForm(instance=request.user)
        data={'form':formulario}
        return render(request, 'edit_profile.html',data)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
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