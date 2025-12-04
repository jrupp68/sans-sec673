import pyWars
import re
import zoneinfo
from datetime import datetime

d = pyWars.exercise("https://live.sec673.com:10000")
d.login('jrupp@acuity.com', 'xBogztGy7#$#BKcA')
input = d.data(49)
answer = []

def convert_timestamp(input):
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7,
              'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    log = input[0]
    
    attacker_timezone = zoneinfo.ZoneInfo(input[1])
    
    log_timestamp = re.findall('\[.+\]', log)[0]
    x = datetime.strptime('[%d/%b/%Y:%H:%M:%S %z]', log_timestamp)

    log_year = int(re.findall('\d{4}', log_timestamp)[0])
    log_month_str = re.findall('\w{3}', log_timestamp)[0]
    log_month = months[log_month_str]
    log_hour = int(log_timestamp[13:15])
    log_min = int(log_timestamp[16:18])
    log_sec = int(log_timestamp[19:21])
    log_day = int(log_timestamp[1:3])
    log_timestamp_offset = log_timestamp.split(' ')[1][:-1]
    attacker_utc = datetime(log_year, log_month, log_day, log_hour, log_min, log_sec, tzinfo=attacker_timezone )
    pass

for item in input:
    convert_timestamp(item)
    exit()


# print(len(input),input)
# print(len(answer), answer)
# response = d.answer(answer)
# print(response)
# d.logout()
# exit()