import contextlib
from datetime import datetime, timedelta
from typing import List
import pytz
from pytz import timezone
from datetime import date, time, datetime
import django.utils.timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
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
    duracion_cita = models.IntegerField('Duracion de Hora en Minutos',default=60,null=True,blank=True)
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "Medico"
        timezone=pytz.timezone("America/Santiago")
    
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
        dia_de_termino.strftime('%d-%m-%Y')
        dia_de_termino=self.start_date.strftime('%d-%m-%Y')
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
        hora_inicio=self.start.strftime('%H:%M:%S')
        return hora_inicio

    def hora_termino(self):
        hora_termino=self.end.strftime('%H:%M:%S')
        return hora_termino 

    def dia(self):
        dia=self.start.strftime('%d-%m-%Y')
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
        return self.booking.owner.nombre+' '+self.booking.owner.apellido_paterno+' '+self.booking.owner.apellido_materno

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
        rut=self.booking.owner
        return rut
    def numero_telefono(self):
        numero=str(self.booking.owner.telefono_contacto)
        return numero
    def correo_electronico(self):
        correo_electronico=self.booking.owner.email
        return correo_electronico
    class Meta:
        verbose_name = "Horario Bloqueado"
        verbose_name_plural = "Horarios Bloqueados"

class Agendamiento(AbstractBooking):
    class AgendaMeta:
        schedule_model = Medico

    owner = models.ForeignKey(
        to=UsuarioPaciente,
        on_delete=models.PROTECT,
        related_name="reservations",
    )
    start_time = models.DateTimeField('Hora de Inicio',db_index=True)
    end_time = models.DateTimeField('Hora de Termino',db_index=True)
    approved = models.BooleanField('Confirmada',default=False)

    def get_reserved_spans(self):
        # we only reserve the time if the reservation has been approved
        if self.approved:
            yield TimeSpan(self.start_time, self.end_time)
    
    def nombre_paciente(self):
        return self.owner.nombre+' '+self.owner.apellido_paterno+' '+self.owner.apellido_materno

    def hora_inicio(self):
        hora_inicio=self.start_time.astimezone(timezone('America/Santiago')).strftime('%H:%M:%S')
        return hora_inicio

    def hora_termino(self):
        hora_termino=self.end_time.astimezone(timezone('America/Santiago')).strftime('%H:%M:%S')
        return hora_termino 

    def dia_de_cita(self):
        dia_de_cita=self.start_time.astimezone(timezone('America/Santiago')).strftime('%d-%m-%Y')
        return dia_de_cita
 
    def paciente(self):
        rut=self.owner
        return rut
    def numero_telefono(self):
        numero=str(self.owner.telefono_contacto)
        return numero
    def correo_electronico(self):
        correo_electronico=self.owner.email
        return correo_electronico
    class Meta:
        verbose_name = "Cita Agendada"
        verbose_name_plural = "Citas Agedadas"