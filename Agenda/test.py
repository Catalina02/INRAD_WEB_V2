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
#Obtener de clase Disponibilidad
DUR = timedelta(minutes=60)
padding=timedelta(minutes=15)

#Ingresa el Usuario en el FORMS Agendamiento
dia=date.today()
testday=datetime.strptime('2021-12-01 12:00:00','%Y-%m-%d %H:%M:%S').localize('UTC')
medico=Medico.objects.all()[0]
d=Disponibilidad.objects.filter(Medico_id=medico)[0]
dd=DiasDisponibles.objects.filter(Medico_id=medico)
dd=DiasDisponibles.objects.filter(start=testday)
start=dd.start
end=dd.end

start=a.dia.strftime('%Y%m%d ')+a.horarios[:5] 
start_date=datetime.strptime(a.dia.strftime('%Y%m%d ')+a.horarios[:5] ,'%Y%m%d %H:%M').astimezone(timezone('UTC')) 
start_date

def daterange(start, end,delta,padding):
    while start < end:
        if (start+delta)<end:
            yield start
            start = start+delta+padding
        else:
            break

list_time=[]
for single_date in daterange(start, end,DUR,padding):
    list_time.append(single_date.astimezone(timezone('America/Santiago')).strftime("%H:%M")+'-'+(single_date+DUR).astimezone(timezone('America/Santiago')).strftime("%H:%M"))


#only for test
for single_date in daterange(start, end,DUR,padding):
    print(TimeSpan(single_date, (single_date+DUR)))