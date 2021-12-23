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
#obtener rango horario de disponibilidad
Disponibilidad.objects.filter(id=a.schedule_id)[0].start_time
Disponibilidad.objects.filter(id=a.schedule_id)[0].end_time
#Obtener dias disponibles asociada a CitaAgendada
DiasDisponibles.objects.filter(availability_id=a.schedule_id)