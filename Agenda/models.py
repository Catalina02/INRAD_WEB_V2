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

class Availability(AbstractAvailability):
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "Medico"
        timezone=pytz.timezone("America/Santiago")


class AvailabilityOccurrence(AbstractAvailabilityOccurrence):
    class AgendaMeta:
        availability_model = Availability
        schedule_model = Medico
        schedule_field = "Medico"


class Slot(AbstractTimeSlot):
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "Medico"
        booking_model = "agendamiento"
        availability_model = Availability


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