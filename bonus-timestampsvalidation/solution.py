import pyWars
from datetime import datetime, timedelta

def day_of_week_from_day_of_year(year: int, day_of_year: int) -> str:
    date = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)
    return date.strftime("%A")  # full weekday name

d = pyWars.exercise("https://live.sec673.com:10000")
d.login('jrupp@acuity.com', 'xBogztGy7#$#BKcA')
input = d.data(43)

answer = list()
for eachstring in input:
    weekday = eachstring.split(' ')[0]
    day_of_year = int(eachstring.split(' ')[1])
    year = int(eachstring.split(' ')[5])
    if day_of_week_from_day_of_year(year, day_of_year) == weekday:
        answer.append(eachstring)

response = d.answer(answer)
d.logout()