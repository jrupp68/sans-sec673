import datetime
import time

now = datetime.datetime.now()
my_offset = time.localtime().tm_gmtoff//60//60
for i in range(14, -12, -1 ):
    tzrecord = datetime.timezone(datetime.timedelta(hours=i))
    tz_aware = datetime.datetime.now(tzrecord)
    relative = i - my_offset
    print(f"{tz_aware.tzname(): <13s}  {str(tz_aware)}  {relative:0=+3d} from you")
