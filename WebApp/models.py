from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
# Create your models here.


#******CONTACTO ****************************************

opciones_contacto=[
    ('radioterapia','RADIOTERAPIA'),
    ('radiocirujia','RADIOCIRUGÍA'),
    ('braquiterapia','BRAQUITERAPIA'),
    ('fotodinamia','FOTODINAMIA'),
    ('otros','OTROS'),
]
class Mensaje(models.Model):
    nombre=models.CharField(max_length=100)
    telefono_contacto=PhoneNumberField()
    correo_contacto=models.EmailField(null=False, blank=False)
    tipo_contacto=models.CharField(choices=opciones_contacto,max_length = 20,)
    mensaje=models.TextField()
    paciente_contactado=models.BooleanField(null=False,default=False)
    fecha_contacto=models.DateField(null=True)
  

    def __str__(self):
        return self.nombre