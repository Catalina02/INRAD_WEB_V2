import contextlib
from datetime import datetime, timedelta
from typing import List
import pytz
from datetime import date, time, datetime
import django.utils.timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

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
        timezone=pytz.timezone("America/Santiago")


class DiasDisponibles(AbstractAvailabilityOccurrence):
    class AgendaMeta:
        availability_model = Disponibilidad
        schedule_model = Medico
        schedule_field = "Medico"
    

class AgendaOcupada(AbstractTimeSlot):
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "Medico"
        booking_model = "agendamiento"
        availability_model = Disponibilidad

from pytz import timezone
class Agendamiento(AbstractBooking):
    class AgendaMeta:
        schedule_model = Medico

    owner = models.ForeignKey(
        to=UsuarioPaciente,
        on_delete=models.PROTECT,
        related_name="reservations",
    )
    start_time = models.DateTimeField(db_index=True)
    end_time = models.DateTimeField(db_index=True)
    approved = models.BooleanField(default=False)

    def get_reserved_spans(self):
        # we only reserve the time if the reservation has been approved
        if self.approved:
            yield TimeSpan(self.start_time, self.end_time)
    
    def paciente(self):
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
 