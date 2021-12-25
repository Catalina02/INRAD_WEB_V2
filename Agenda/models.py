import contextlib
from datetime import datetime, timedelta
from typing import List
from django.db.models.deletion import CASCADE
import pytz
from pytz import timezone
from datetime import date, time, datetime
import django.utils.timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CharField, Model

from django.utils.translation import gettext_lazy as _
from dateutil.relativedelta import relativedelta
from django_agenda.time_span import TimeSpan
from Users.models import *
from django_agenda.models import (
    AbstractAvailability,
    AbstractAvailabilityOccurrence,
    AbstractTimeSlot,
    AbstractBooking,
)

class Disponibilidad(AbstractAvailability):
    verbose_name='Agenda'
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "Medico"
    
    def nombre_medico(self):
        return self.Medico.nombre+' '+self.Medico.apellido_paterno+' '+self.Medico.apellido_materno

    def hora_inicio(self):
        hora_inicio=self.start_time.strftime('%H:%M:%S')
        return hora_inicio

    def hora_termino(self):
        hora_termino=self.end_time.strftime('%H:%M:%S')
        return hora_termino 

    def dia_de_inicio(self):
        dia_de_inicio=self.start_date.strftime('%d-%m-%Y')
        return dia_de_inicio

    def dia_de_termino(self):
        start_str=self.start_date.strftime('%Y%m%d')
        start_date=datetime.strptime(start_str,'%Y%m%d')
        delta=relativedelta(months=+1)
        dia_de_termino=start_date+delta
        dia_de_termino=dia_de_termino.strftime('%d-%m-%Y')
        return dia_de_termino
    def numero_telefono(self):
        numero=str(self.Medico.telefono_contacto)
        return numero
    def correo_electronico(self):
        correo_electronico=self.Medico.email
        return correo_electronico
    
    class Meta:
        verbose_name = "Horario de Atención"
        verbose_name_plural = "Horarios de Atención"


class DiasDisponibles(AbstractAvailabilityOccurrence):
    class AgendaMeta:
        availability_model = Disponibilidad
        schedule_model = Medico
        schedule_field = "Medico"

    def nombre_medico(self):
        return self.Medico.nombre+' '+self.Medico.apellido_paterno+' '+self.Medico.apellido_materno

    def hora_inicio(self):
        hora_inicio=self.start.astimezone(timezone('America/Santiago')).strftime('%H:%M:%S')
        return hora_inicio

    def hora_termino(self):
        hora_termino=self.end.astimezone(timezone('America/Santiago')).strftime('%H:%M:%S')
        return hora_termino 

    def __str__(self):
        dia=self.start.astimezone(timezone('America/Santiago')).strftime('%d-%m-%Y')
        return dia

    def numero_telefono(self):
        numero=str(self.Medico.telefono_contacto)
        return numero
    def correo_electronico(self):
        correo_electronico=self.Medico.email
        return correo_electronico
    
    class Meta:
        verbose_name = "Dia de Atención"
        verbose_name_plural = "Dias de Atención"

class AgendaOcupada(AbstractTimeSlot):
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "Medico"
        booking_model = "agendamiento"
        availability_model = Disponibilidad
    def nombre_paciente(self):
        return self.booking.paciente.nombre+' '+self.booking.paciente.apellido_paterno+' '+self.booking.paciente.apellido_materno

    def hora_inicio(self):
        hora_inicio=self.start.astimezone(timezone('America/Santiago')).strftime('%H:%M:%S')
        return hora_inicio

    def hora_termino(self):
        hora_termino=self.end.astimezone(timezone('America/Santiago')).strftime('%H:%M:%S')
        return hora_termino 

    def dia_de_cita(self):
        dia_de_cita=self.start.astimezone(timezone('America/Santiago')).strftime('%d-%m-%Y')
        return dia_de_cita
 
    def paciente(self):
        rut=self.booking.paciente
        return rut
    def numero_telefono(self):
        numero=str(self.booking.paciente.telefono_contacto)
        return numero
    def correo_electronico(self):
        correo_electronico=self.booking.paciente.email
        return correo_electronico
    def medico_a_cargo(self):
        return self.Medico.nombre+' '+self.Medico.apellido_paterno+' '+self.Medico.apellido_materno
    class Meta:
        verbose_name = "Horario Bloqueado"
        verbose_name_plural = "Horarios Bloqueados"

class Agendamiento(AbstractBooking):
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "Medico"
    HORARIOS=[
    ('8:00-8:45','8:00-8:45'),
    ('9:00-9:45','9:00-9:45'),
    ('10:00-10:45','10:00-10:45'),
    ('11:00-11:45','11:00-11:45'),
    ('12:00-12:45','12:00-12:45'),
    ('13:00-13:45','13:00-13:45'),
    ('14:00-14:45','14:00-14:45'),
    ('15:00-15:45','15:00-15:45'),
    ('16:00-16:45','16:00-16:45'),
    ('17:00-17:45','17:00-17:45'),
    ('18:00-18:45','18:00-18:45'),
    ('19:00-19:45','19:00-19:45'),
    ]
    horarios = models.CharField(max_length=16, choices=HORARIOS)
    paciente = models.ForeignKey(
        to=UsuarioPaciente,
        on_delete=models.PROTECT,
        related_name="reservations",
    )
    dia=  models.DateField('Dia de Consulta',blank=False,db_index=True,null=False)
    hora_de_inicio=  models.TimeField('Hora de Inicio',blank=True,db_index=True,null=True)
    hora_de_termino=  models.TimeField('Hora de Termino',blank=True,db_index=True,null=True)
    start_time = models.DateTimeField(db_index=True,blank=True,null=True,default=datetime.now())
    end_time = models.DateTimeField(db_index=True,blank=True,null=True,default=datetime.now())
    approved = models.BooleanField('Confirmada',default=False)
    disponibilidad =models.ForeignKey(Disponibilidad, on_delete = models.CASCADE,blank=True,null=True)
    
    #medico=models.ForeignKey(Medico, on_delete = models.CASCADE,blank=False,null=True)

    def get_reserved_spans(self):
        # we only reserve the time if the reservation has been approved
        if self.approved:
            yield TimeSpan(self.start_time, self.end_time)
    
    def nombre_paciente(self):
        return self.paciente.nombre+' '+self.paciente.apellido_paterno+' '+self.paciente.apellido_materno

    def hora_inicio(self):
        hora_inicio=self.start_time.astimezone(timezone('America/Santiago')).strftime('%H:%M:%S')
        return hora_inicio

    def hora_termino(self):
        hora_termino=self.end_time.astimezone(timezone('America/Santiago')).strftime('%H:%M:%S')
        return hora_termino 

    def dia_de_cita(self):
        dia_de_cita=self.start_time.astimezone(timezone('America/Santiago')).strftime('%d-%m-%Y')
        return dia_de_cita
 
    def rut_paciente(self):
        rut=self.paciente.rut_usuario
        return rut
    def numero_telefono(self):
        numero=str(self.paciente.telefono_contacto)
        return numero
    def correo_electronico(self):
        correo_electronico=self.paciente.email
        return correo_electronico
    def medico_a_cargo(self):
        return self.schedule.nombre+' '+self.schedule.apellido_paterno+' '+self.schedule.apellido_materno
    class Meta:
        verbose_name = "Cita Agendada"
        verbose_name_plural = "Citas Agedadas"