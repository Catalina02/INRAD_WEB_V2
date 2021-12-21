import contextlib
from datetime import datetime, timedelta
from typing import List

import django.utils.timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_agenda.time_span import TimeSpan
from Users.models import Medico, Paciente, Administrativo
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


class AvailabilityOccurrence(AbstractAvailabilityOccurrence):
    class AgendaMeta:
        availability_model = Availability
        schedule_model = Medico
        schedule_field = "Medico"


class Slot(AbstractTimeSlot):
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "Medico"
        booking_model = "booking"
        availability_model = Availability

class Booking(AbstractBooking):
    class AgendaMeta:
        schedule_model = Medico
        schedule_field = "schedule"

    DURATION = timedelta(minutes=60)

    Paciente = models.ForeignKey(
        verbose_name=_("guest"),
        to=Paciente,
        on_delete=models.PROTECT,
        related_name="+",
    )
    def __init__(self, *args, **kwargs):
        self.loading = True
        super().__init__(*args, **kwargs)
        self.loading = False
        self.__editor = None
        self.allow_multiple_bookings = False

    def clean(self):
        super().clean()
        # check for duplicates
        dup_q = models.Q(schedule=self.schedule, guest=self.guest, state=self.state)
        if self.id is not None:
            dup_q &= ~models.Q(id=self.id)

        sub_q = models.Q()
        if self.requested_time_1 is not None:
            sub_q |= models.Q(requested_time_1=self.requested_time_1) | models.Q(
                requested_time_2=self.requested_time_1
            )
        if self.requested_time_2 is not None:
            sub_q |= models.Q(requested_time_1=self.requested_time_2) | models.Q(
                requested_time_2=self.requested_time_2
            )
        dup_q &= sub_q

        if Booking.objects.filter(dup_q).exists():
            raise ValidationError(_("Duplicate booking"))

    def get_padding(self):
        return self.padding

    def is_booked_slot_busy(self):
        return not self.allow_multiple_bookings

    def get_requested_times(self):
        for time in (self.requested_time_1, self.requested_time_2):
            if time is not None:
                yield time

    def get_reserved_spans(self):
        """
        Return a list of times that should be reserved
        """
        if self.state in self.RESERVED_STATES:
            for time in self.get_requested_times():
                yield TimeSpan(time, time + self.DURATION)


