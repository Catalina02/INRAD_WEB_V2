availability1 = Availability.objects.create(
            start_date=date(2001, 1, 1),
            start_time=time(8),
            end_time=time(15),
            recurrence="RRULE:FREQ=WEEKLY",
            schedule=medico,
            timezone=pytz.timezone("America/Santiago"),
        )
from dateutil.relativedelta import relativedelta

start_str=start_date.strftime('%Y%m%d')
start_date=datetime.strptime(start_str,'%Y%m%d')
delta=relativedelta(months=+1)
end_date=start_date+delta
end_date.strftime('%d-%m-%Y')

from datetime import datetime, timezone
import pytz

from datetime import datetime
import pytz
local_tz = pytz.timezone('America/Santiago')
start_date = local_tz.localize(start_date)
end_date = local_tz.localize(end_date)

#imprimir atributos
from pprint import pprint
pprint(dir(a))

#obtener primer agendamiento
a=Agendamiento.objects.all()[0]
#Obtener disponibilidad asociada a CitaAgendada
Disponibilidad.objects.filter(id=a.schedule_id)
Disponibilidad.objects.all()
#obtener rango horario de disponibilidad
Disponibilidad.objects.filter(id=a.schedule_id)[0].start_time
Disponibilidad.objects.filter(id=a.schedule_id)[0].end_time
#Obtener dias disponibles asociada a CitaAgendada
DiasDisponibles.objects.filter(availability_id=a.schedule_id)

'''Pasos para agendar cita'''
#identificar dia y medico
a.dia #Dia->datetime.date(2021, 12, 23)
a.schedule_id #agenda asociada
#buscar dia
DiasDisponibles.objects.filter(availability_id=a.schedule_id)[0].start #->datetime.datetime(2021, 12, 1, 9, 0, tzinfo=<UTC>)
#compatibilizar formatos
a_new=a.dia.strftime('%Y%m%d') #->'20211223'
a_2=datetime.strptime(a_new,'%Y%m%d')#-> datetime.datetime(2021, 12, 23, 0, 0)
a_dia=a_2.astimezone(timezone('UTC'))#->datetime.datetime(2021, 12, 23, 3, 0, tzinfo=<UTC>)

for i in DiasDisponibles.objects.filter(availability_id=a.schedule_id):
    i_day=i.start.strftime('%Y%m%d')
    i_day=datetime.strptime(i_day,'%Y%m%d').astimezone(timezone('UTC'))
    if (i_day==a_dia):
        start_time=i.start.strftime('%H:%M:%S')
        start_time=datetime.strptime(start_time,'%H:%M:%S')
        end_time=i.end.strftime('%H:%M:%S')
        end_time=datetime.strptime(end_time,'%H:%M:%S')
        print(start_time)
        print(end_time)

'''
Nuevas Pruebas
Bansadnose en el modelo basico, el cual esta bueno, dividir la Disponibilidad en horas, modificando el Modelo Dias Discponibles
'''
from django_agenda.time_span import TimeSpan
from datetime import datetime, timedelta
from Agenda.models import *
from Users.models import *

DUR = timedelta(minutes=60)
dd=DiasDisponibles.objects.all()[0]
start=dd.start
end=dd.end

def daterange(start, end,delta):
    while start < end:
        yield start
        start = start+delta


for single_date in daterange(start, end,DUR):
    print(single_date.strftime("%H:%M")+'-'+(single_date+DUR).strftime("%H:%M"))