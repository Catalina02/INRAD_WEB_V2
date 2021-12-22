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
end_date=start+delta

from datetime import datetime, timezone
import pytz

from datetime import datetime
import pytz
local_tz = pytz.timezone('America/Santiago')
start_date = local_tz.localize(start)
end_date = local_tz.localize(end_date)