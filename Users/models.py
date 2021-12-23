from django.contrib.auth.models import AbstractUser,BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    
    def create_user(self, rut, email, password=None):

        if rut is None:
            raise TypeError('Debe indicar s RUT')

        if email is None:
            raise TypeError('Debe Indicar su Email')

        usuario = Usuario.objects.create(
        email=self.normalize_email(email),
        rut=rut,
        password = make_password(password))
        
        return usuario

    def create_superuser(self,email,rut,dv,password):
        usuario=self.create_user(rut,email,password=password)
        usuario.is_superuser=True
        usuario.is_staff=True
        
        usuario.save()
        return usuario

class Usuario(AbstractUser):
    #new Fields
    rut=models.IntegerField(null=False, blank=False, unique=True)
    dv=models.CharField(max_length=1,null=False)
    
    nombre=models.CharField('Nombre',max_length=100,null=False)
    apellido_paterno=models.CharField('Apellido Paterno',max_length=100)
    apellido_materno=models.CharField('Apellido Materno',max_length=100)
    
    email = models.EmailField('Correo Electronico',unique=True)
    telefono_contacto=PhoneNumberField(null=False, blank=False)
    telefono_contacto_2=PhoneNumberField(null=True,default='',blank=True)
    fecha_nacimiento=models.DateField(null=True,blank=True)
    
    prevision=models.CharField('Prevision',max_length=50,null=False,blank=True)
    domicilio=models.CharField('Domicilio',max_length=255,null=False,blank=True)

    foto_perfil=models.ImageField('Foto de Perfil',upload_to='Usuarios/',null=True,default='blank-profile-picture-973460_640.png',blank=True)
    opciones_sexo=[
            ('mujer','Mujer'),
            ('hombre','Hombre'),
            ('ninguno','Prefiero no Responder'),
        ]

    sexo=models.CharField(choices=opciones_sexo,max_length = 25,default='ninguno')
    #django flieds
    username=None
    first_name=None
    last_name=None

    date_joined=models.DateField('Fecha Ingreso al Sistema',null=True,blank=True)

 

    #definir tipos
    class Types(models.TextChoices):
        UsuarioPaciente='UsuarioPaciente','UsuarioPaciente'
        Medico='Medico','MEDICO'
        Administrativo='Administrativo','ADMINISTRATIVO'
        
    type=models.CharField(_('Tipo de Usuario'),choices=Types.choices, default=Types.UsuarioPaciente,max_length=100)
    
    #definir pk
    objects=UsuarioManager()
    USERNAME_FIELD='rut'
    REQUIRED_FIELDS=['dv','email']
    def __str__(self):
        return str(self.rut)


#CLASE DE UsuarioPaciente
class InformacionMedica(models.Model):
    user = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    alergias= anamnesis=models.TextField('Alergias',max_length=255,null=True,blank=True)
    diagnostico=models.CharField('Diagnostico',max_length=255,null=True,blank=True)
    medico_derivante=models.CharField('Medico Derivante',max_length=255,null=True,blank=True)
    institucion_derivante=models.CharField('Intitucion Derivante',max_length=255,null=True,blank=True)
    medico_INRAD=models.CharField('Medico INRAD',max_length=255,null=True,blank=True)
    anamnesis=models.TextField('Anamnesis',null=True,blank=True)
    UsuarioPaciente_paliativo=models.BooleanField('UsuarioPaciente Paliativo',null=True,blank=True)
class UsuarioPacienteManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs): 
        return super().get_queryset(*args,*kwargs).filter(type=Usuario.Types.UsuarioPaciente)
class UsuarioPaciente(Usuario):
    base_type = Usuario.Types.UsuarioPaciente
    objects=UsuarioPacienteManager()
    class Meta:
        proxy=True
    @property
    def showAdditional(self):
        return self.informacionmedica


#CLASE MEDICO
class MedicoManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs): 
        return super().get_queryset(*args,*kwargs).filter(type=Usuario.Types.Medico)
class Medico(Usuario):
    objects=MedicoManager()
    class Meta:
        proxy=True

#CLASE ADMIN


      
class AdministrativoManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs): 
        return super().get_queryset(*args,*kwargs).filter(type=Usuario.Types.Administrativo)
class Administrativo(Usuario):
    objects=AdministrativoManager()
    class Meta:
        proxy=True