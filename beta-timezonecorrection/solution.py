import pyWars
import re
import zoneinfo
from datetime import datetime

d = pyWars.exercise("https://live.sec673.com:10000")
d.login('jrupp@acuity.com', 'xBogztGy7#$#BKcA')
input = d.data(49)
answer = []

def convert_timestamp(input):
    attacker_timezone = zoneinfo.ZoneInfo(input[1])
    log_pre_string = re.findall('[\d\.]+ - - ', input[0])[0]
    log_timestamp = re.findall('\[.+\]', input[0])[0]
    log_post_string = re.findall('](\s\w+\s\/)', input[0])[0]
    server_dt = datetime.strptime(log_timestamp, '[%d/%b/%Y:%H:%M:%S %z]')
    attacker_dt = server_dt.astimezone(attacker_timezone)
    output_timestamp = attacker_dt.strftime('[%d/%b/%Y:%H:%M:%S %z]')  
    return log_pre_string + output_timestamp + log_post_string          

answer = []
for item in input:
    answer.append(convert_timestamp(item))

print(len(answer), answer)
response = d.answer(answer)
print(response)
d.logout()
exit()